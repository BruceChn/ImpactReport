var React = require('react');
var ReactDOM = require('react-dom');

var Highcharts = require('highcharts');
HighchartsMore = require('highcharts-more')(Highcharts)
require('highcharts/modules/solid-gauge')(Highcharts);
var HighChart = require('./high-chart');


var App = React.createClass({
  getInitialState:function(){
    return{
      overview_options : overview_options,
      average_comparion_options: average_comparion_options,
      container1: 'react-container',
      container2: 'react-container2',
      container3: 'react-container3',
      percentage_options1:percentage_options1
    }
  },
  render:function(){
    console.log(this.state.container);
    return <div>
      <div className = "col-sm-12">
        <HighChart container = {this.state.container1} options = {this.state.overview_options}/>
      </div>
      <div className = "col-sm-6">
        <HighChart container = {this.state.container2} options = {this.state.average_comparion_options}/>
      </div>
      <div className = "col-sm-6">
        <HighChart container = {this.state.container3} options = {this.state.percentage_options1} />
      </div>
  </div>

  }
})
var element = React.createElement(App,{});
ReactDOM.render(element,document.querySelector('.react-charts'));
