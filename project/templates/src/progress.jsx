var React = require('react');
var ReactDOM = require('react-dom');

var Highcharts = require('highcharts');
//HighchartsMore = require('highcharts-more')(Highcharts)
//require('highcharts/modules/solid-gauge')(Highcharts);
var HighChart = require('./high-chart');
var Header = require('./header');


var ProgressTracker = React.createClass({
  getInitialState:function(){
    return {
      progress:progress,
      overall:overall,
      math:math,
      science:science,
      reading:reading,
      writing:writing,
      container1:"react-container1",
      container2:"react-container2",
      container3:"react-container3",
      container4:"react-container4",
      container5:"react-container5",
      container6:"react-container6",
    }
  },
  render:function(){
    return <div>
      <div className = "chart-wrapper0">
        <HighChart options = {this.state.progress} container = {this.state.container1}/>
        <HighChart options = {this.state.overall} container = {this.state.container2}/>
      </div>
      <h1 style = {{textAlign:"center"}}>Percentage Level Complete</h1>
      <div className = "chart-wrapper">

        <HighChart options = {this.state.math} container = {this.state.container3}/>

        <HighChart options = {this.state.science} container = {this.state.container4}/>
      </div>
      <div className = "chart-wrapper">
        <HighChart options = {this.state.reading} container = {this.state.container5}/>
        <HighChart options = {this.state.writing} container = {this.state.container6}/>
      </div>
    </div>
  }
});

var element1 = React.createElement(Header,{title:pageTitle});
var element2 = React.createElement(ProgressTracker,{});
ReactDOM.render(element2,document.querySelector('.react-charts'));
ReactDOM.render(element1,document.querySelector('.header'));
