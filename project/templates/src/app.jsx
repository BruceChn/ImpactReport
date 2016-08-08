var React = require('react');
var ReactDOM = require('react-dom');
var Highcharts = require('highcharts');
//require('highcharts/modules/bar')(Highcharts);
var HighChart = require('./high-chart');

var App = React.createClass({
  getInitialState:function(){
    return{
      options:{
        chart: {
          type: 'bar',
        },

        title: {
          text: "User's Overview",
        },
        xAxis:{
          categories:['Writing Score','Science Score','Math Score','Reading Score','Current Overall Score','Best Overall Score To Date'],
          title:{
            text:null
          }
        },
        color:['#A9A9A9','#A9A9A9','#A9A9A9','#A9A9A9','#1E90FF','#6B8E23'],
        yAxis:{
          min:0,
          title:{
            text:null
          },
          max:1200
        },
        series: [{
          showInLegend:false,
          name:"score",
          data: [{
            y:100,
            color:'#A9A9A9'
            },
            {
              y:400,
              color:'#A9A9A9'
            },
            {
              y:500,
              color:'#A9A9A9'
            },
            {
              y:600,
              color:'#A9A9A9'
            },
            {
              y:900,
              color:'#1E90FF'
            },
            {
              y:1100,
              color:'#6B8E23'
            }]

        }]
      },
      container: 'react-container'
    }
  },
  render:function(){
    console.log(this.state.container);
    return <HighChart container = {this.state.container} options = {this.state.options}/>

  }
})
var element = React.createElement(App,{});
ReactDOM.render(element,document.querySelector('.react-charts'));
