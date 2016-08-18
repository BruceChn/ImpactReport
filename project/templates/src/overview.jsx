var React = require('react');
var ReactDOM = require('react-dom');

var Highcharts = require('highcharts');
HighchartsMore = require('highcharts-more')(Highcharts)
require('highcharts/modules/solid-gauge')(Highcharts);
var HighChart = require('./high-chart');
var Header = require('./header');



var Overview = React.createClass({
  getInitialState:function(){
    return{
      overview_options : overview_options,
      average_comparion_options: average_comparion_options,
      container1: 'react-container1',
      container2: 'react-container2',
      container3: 'react-container3',
      container4: 'react-container4',
      container5: 'react-container5',
      percentage_options1:percentage_options1,
      regional_average_options:regional_average_options,
      percentage_options2:percentage_options2
    }
  },
  render:function(){

    return <div>

      <HighChart container = {this.state.container1} options = {this.state.overview_options}/>

      <div className = "chart-wrapper">
      <HighChart container = {this.state.container2} options = {this.state.average_comparion_options}/>


      <HighChart container = {this.state.container3} options = {this.state.percentage_options1} />
      </div>
      <div className = "chart-wrapper">
      <HighChart container = {this.state.container4} options = {this.state.regional_average_options}/>


      <HighChart container = {this.state.container5} options = {this.state.percentage_options2} />
      </div>
  </div>

  }
});

var element = React.createElement(Overview,{});
var element1 = React.createElement(Header,{title:pageTitle});

ReactDOM.render(element,document.querySelector('.react-charts'));
ReactDOM.render(element1,document.querySelector('.header'));
