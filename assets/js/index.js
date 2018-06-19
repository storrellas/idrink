var React = require('react')
var ReactDOM = require('react-dom')
var createReactClass = require('create-react-class');
var superagent = require('superagent')

var Hello = createReactClass ({
    render: function() {
        return (
            <h1>
            Hello, React!
            </h1>
        )
    }
})

ReactDOM.render(<Hello />, document.getElementById('container'))

var DrinkProgressEnum = {
  PENDING: 1,
  ONGOING: 2,
  DONE: 3,
};
class DrinkDetail extends React.Component {

  constructor(props){
    super(props)

    // Create property to be passed to
    this.drink_start_handler = this.drink_start_handler.bind(this);
    this.drink_done_handler = this.drink_done_handler.bind(this);
    this.state = {
      drink_generation : this.props.drink_generation
    }

    this.serving = {
      id : 0
    }
    this.polling_timer = 1000
  }
  componentWillReceiveProps(nextProps){
    //console.log("componentWillReceiveProps" + JSON.stringify(nextProps))
    this.state.drink_generation = DrinkProgressEnum.PENDING
  }

  drink_start_handler(){

    // Request to create Drink
    superagent
      .post('/combiner/serving/')
      .send({ drink: this.props.id })
      .set('X-API-Key', 'foobar')
      .set('Accept', 'application/json')
      .then((res) => {
         // console.log("Setting Serving id to " + res.body.id)
         // console.log(JSON.stringify(res.body))
         this.serving.id = res.body.id
      });

    this.setState({
      drink_generation : DrinkProgressEnum.ONGOING
    })

    // Simulate message to Backend
    setTimeout(this.drink_done_handler, this.polling_timer)
  }

  drink_done_handler(){

    // Request to create Drink
    superagent
      .get('/combiner/serving/' + this.serving.id + '/')
      .set('X-API-Key', 'foobar')
      .set('Accept', 'application/json')
      .then((res) => {
         //console.log("Getting state from  " + res.body.id)
         //console.log(JSON.stringify(res.body))
         if( res.body.completed ){
           // Change state and redraw
           this.setState({
              drink_generation : DrinkProgressEnum.DONE
            })
         }else{
           // Request again after a while
           setTimeout(this.drink_done_handler, this.polling_timer)
         }
      });
  }

  render() {
    var button_content = ""
    var button_class = "btn btn-primary"
    switch(this.state.drink_generation) {
        case DrinkProgressEnum.DONE:
            button_content = "DONE!"
            button_class = "btn btn-success"
            break;
        case DrinkProgressEnum.ONGOING:
            button_content = <i className="fa fa-spinner fa-spin"></i>
            break;
        default:
            button_content = "Make Drink"
    }


    return (
      <div className="modal fade" id="drink_modal" tabIndex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div className="modal-dialog" role="document">
          <div className="modal-content">
            <div className="modal-header">
              <h2 className="modal-title" id="drink_modal">{this.props.name}</h2>
              <button type="className" className="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div className="modal-body">
                <div className="row">
                    <div className="col-md-6">
                        <img src={this.props.image}/>
                    </div>
                     <div className="col-md-6">
                         <p>{this.props.description}</p>
                         <ul>
                           {this.props.ingredient_list}
                         </ul>
                     </div>
                 </div>
            </div>
            <div className="modal-footer">
              <button type="button" className="btn btn-secondary" data-dismiss="modal">Cancel</button>
              <button type="button" className={button_class} onClick={this.drink_start_handler}>
                {button_content}
              </button>
            </div>
          </div>
        </div>
      </div>
    )
  }


}

class Drink extends React.Component {

  render() {
    var imgStyle = {
      zIndex: "2",
      position: "relative"
    };

    return (
      <div className="col-md-4">
          <div className="text-center single-content" onClick={() => this.props.onClick(this.props.index)}>
                <img className="img-thumbnail" src={this.props.image} style={imgStyle}/>
                <h3>{this.props.name}</h3>
                <p>{this.props.description}</p>
            </div>
      </div>
    )
  }
}

class DrinkMatrix extends React.Component {

  constructor(props){
    super(props)

    // Create property to be passed to
    this.showModal = this.showModal.bind(this);

    // Default item list
    this.item_list_size = 6
    this.item_list = []
    for(var i = 0; i < this.item_list_size; i++)
      this.item_list.push(<Drink icon="fa fa-spinner fa-spin" onClick={this.showModal}/>)

    // Stores recipe list
    this.recipe_list = []

    this.drink = {
      name : "MyName",
      image : "MyImage",
      description : "MyDescription",
      ingredient_list : []
    }

  }

  showModal(index) {

    // Generate modal
    var item = this.recipe_list[index]
    this.drink.id = item.id
    this.drink.name = item.name
    this.drink.image = item.image
    this.drink.description = item.description
    this.drink.ingredient_list = []
    item.ingredient_list.forEach( (item, index) => {
      var text = item.size + ' ml of ' + item.name
      this.drink.ingredient_list.push(<li key={index}>{text}</li>)
    });

    // Re-reder component
    this.forceUpdate()

    // Show modal
    $("#drink_modal").modal();
  }

  componentDidMount() {
    superagent
      .get('/combiner/drink/?count=' + this.item_list_size)
      .send({ name: 'Manny', species: 'cat' })
      .set('X-API-Key', 'foobar')
      .set('Accept', 'application/json')
      .then((res) => {
         // console.log(JSON.stringify(res.body))

         // Store recipe list for latter use
         this.recipe_list = res.body

         // Clear item list and redo
         this.item_list = []
         res.body.forEach( (item, index) => {
            this.item_list.push(<Drink index={index}
                                        name={item.name}
                                        image={item.image}
                                        description={item.description}
                                        onClick={this.showModal}/>)
         });

         // Force render() to be called
         this.forceUpdate()

      });

  }

  render() {

    return (
      <div className="container">
        <div className="row">
          {this.item_list[0]}
          {this.item_list[1]}
          {this.item_list[2]}
        </div>
        <div className="row">
          {this.item_list[3]}
          {this.item_list[4]}
          {this.item_list[5]}
        </div>
        <DrinkDetail id={this.drink.id}
                     name={this.drink.name}
                     image={this.drink.image}
                     description={this.drink.description}
                     ingredient_list={this.drink.ingredient_list}/>
      </div>
    )
  }
}


// Render Items
ReactDOM.render( <DrinkMatrix />, document.getElementById('root'));
