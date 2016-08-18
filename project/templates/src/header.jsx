var React = require('react');

module.exports = React.createClass({
  render:function(){
    return <div className = "row">
      <div className = "col-xs-4">
        <img className = "image" id = "logo" src = "static/image/icon TSOG.png"/>
      </div>
      <div className = "col-xs-8">
        <img className = "image" id = "poster" src = "static/image/poster.png"/>
        <h2 style = {{textAlign:"center"}}>
          {this.props.title}
        </h2>
        <div className = "col-xs-6 col-xs-offset-3">
          <p style ={{textAlign : "center",border:"0.1em solid black"}}>
            Level 1
          </p>

        </div>



      </div>
    </div>
  }

});
