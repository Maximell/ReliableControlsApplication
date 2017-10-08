var AppDispatcher = require('../dispatcher/dispatcher');
var EventEmitter = require('events').EventEmitter;
var merge = require('react/lib/merge');

// Internal faults object
var _faults = {}

function receiveFaults(data) {
  _faults = data.faults;
}

var FaultStore = merge(EventEmitter.prototype, {
  // Return all faults
  getFaults: function() {
    return _faults;
  }

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

// Register Dispatcher CallBack
AppDispatcher.register(function(payload) {
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
})

module.exports = FaultStore;
