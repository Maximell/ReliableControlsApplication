var React = require('react');
// var FaultStore = require('../stores/FaultStore');

// // Method to retreive application state from store
// function getAppState() {
//   // return {
//   //   faults: FaultStore.getFaults()
//   // };
//   return {
//     faults: {
//       "device1": 4,
//       "device2": 86
//     }
//   }
// }
//
var FaultList = React.createClass({

  //Set initial state
  getInitialState: function() {
    return getAppState();
  },

  // Listen for changes
  componentDidMount: function() {
    FaultStore.addChangeListener(this._onChange);
  },

  // Unbind change listener
  componentWillUnmount: function() {
    FaultStore.removeChangeListener(this._onChange);
  },

  _renderFaults: function() {
    return <li>fault</li>;
  },

  render() {
    return <ul>{this._renderFaults()}</ul>;
  },

  // Update view when change event is received
  _onChange: function() {
    this.setState(getAppState());
  }
});

export default FaultList;
