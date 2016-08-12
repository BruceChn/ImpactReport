var React = require('react');
var ReactDOM = require('react-dom');

var Highcharts = require('highcharts');
//HighchartsMore = require('highcharts-more')(Highcharts)
//require('highcharts/modules/solid-gauge')(Highcharts);
var HighChart = require('./high-chart');
var Header = require('./header');

var Report = React.createClass({
  getInitialState:function(){
    return {
      report:report,
      container:"react-container1"
    }
  },
  render:function(){
    return<div>
      <div className = "col-sm-12">
        <HighChart options = {this.state.report} container = {this.state.container}/>
      </div>
      <div className = "col-sm-12" >
          <h2 style = {{textAlign:"center",textDecoration:'underline'}}><b>Kindergarten Readiness Report</b></h2>
          <p>
            Reading: <span style ={{color:"#008000"}}>Highly Proficient</span>
          </p>
          <p>
            Writing: <span style ={{color:"#90EE90"}}>Highly Proficient</span>
          </p>
          <p>
            Math: <span style ={{color:"#FF0000"}}>Highly Proficient</span>
          </p>
          <p>
            Science: <span style ={{color:"#FFA500"}}>Highly Proficient</span>
          </p>
          <br/>
          <p>
            Summary:
          </p>
          <p>
            Bruce is ready to attend kindergarten!
          </p>
          <br/>
          <p>
            Warnings:
          </p>
          <ul>
            <li> Math is below proficient, please encourage your child to play more Math related games</li>
          </ul>
      </div>
    </div>
  }
});
var element1 = React.createElement(Report,{});
var element2 = React.createElement(Header,{title:pageTitle});
ReactDOM.render(element1,document.querySelector('.react-charts'));
ReactDOM.render(element2,document.querySelector('.header'));
