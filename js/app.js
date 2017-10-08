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
var _faults = {}

function receiveFaults(data) {
  _faults = data.faults;
}

var FaultStore = merge(EventEmitter.prototype, {
  // Return all faults
  getFaults: function() {
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
    case "FAULTS_RECEIVED":
      receiveFaults(action.data);
      break;
    default:
      return true;
  }
  FaultStore.emitChange();
  return true;
});
// END FaultStore Component

// BEGIN FaultList Component
function getAppState() {
  // return {
  //   faults: FaultStore.getFaults()
  // };
  return {
    faults: {
      "device1": 4,
      "device2": 86
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
// END FaultList component

ReactDOM.render(<FaultList/>, document.getElementById('reactEntry'));
