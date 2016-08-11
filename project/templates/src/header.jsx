var React = require('react');

module.exports = React.createClass({
  render:function(){
    return <div className = "row">
      <div className = "col-sm-4">
        <img className = "image" id = "logo" src = "static/image/icon TSOG.png"/>
      </div>
      <div className = "col-sm-8">
        <img className = "image" id = "poster" src = "static/image/poster.png"/>
        <h2 style = {{textAlign:"center"}}>
          {this.props.title}
        </h2>
        <div className = "col-sm-6 col-sm-offset-3">
          <p style ={{textAlign : "center",fontSize:"4em", border:"0.1em solid black"}}>
            Level 1
          </p>

        </div>
        <div className = "col-sm-2" style ={{marginLeft:"-3.6em"}}>
          <p style={{textAlign:"center",fontSize:"4em"}}>
            &rArr;
          </p>

        </div>
      </div>
    </div>
  }

});
