// General Imports
import React from 'react';
import ReactDOM from 'react-dom';
// Imports for FaultStore
var EventEmitter = require('events').EventEmitter;
var merge = require('merge');

// Imports for Dispatcher
const Dispatcher = require('flux').Dispatcher;

// BEGIN Dispatcher Component
var dispatcher = new Dispatcher();
// END Dispatcher Component

// BEGIN FaultStore Component
// Internal faults object
var _faults = 0

function receiveFaults(data) {
  alert("receiveFaults");
  _faults = _faults + 1;
}

var FaultStore = merge(EventEmitter.prototype, {
  // Return all faults
  getFaults: function() {
    receiveFaults();
    return _faults;
  },

  emitChange: function() {
    this.emit('change');
  },

  addChangeListener: function(callback) {
    this.on('change', callback);
  },

  removeChangeListener: function(callback) {
    this.removeListener('change', callback);
  }
});

//Register Dispatcher CallBack
dispatcher.register(function(payload) {
  var action = payload.action;
  // define what to do for certain actions
  switch(action.actionType) {
    case "UPDATE_FAULTS":
      alert("here2");
      receiveFaults(action.data);
      break;
    default:
      return true;
  }
  FaultStore.emitChange();
  return true;
});
// END FaultStore Component


// BEGIN FaultActions
function updateFaults() {
  dispatcher.dispatch({
    "type": "UPDATE_FAULTS",
    "data": {}
  });
}
// END FaultActions


// BEGIN FaultList Component
function getAppState() {
  return {
    faults: {
      faults: FaultStore.getFaults()
    }
  }
}

var FaultList = React.createClass({
  //Set initial state
  getInitialState: function() {
    return getAppState();
  },
  // Listen for changes
  componentDidMount: function() {
    FaultStore.addChangeListener(this._onChange);
    this.interval = setInterval(alert("here5"), 500);
  },
  // Unbind change listener
  componentWillUnmount: function() {
    FaultStore.removeChangeListener(this._onChange);
    clearInterval(this.interval);
  },
  _renderFaults: function() {
    return <li>fault{this.state.faults.faults}</li>;
  },
  render() {
    return <ul>{this._renderFaults()}</ul>;
  },
  // Update view when change event is received
  _onChange: function() {
    alert("change triggered");
    this.setState(getAppState());
  }
});
// END FaultList component

ReactDOM.render(<FaultList/>, document.getElementById('reactEntry'));
