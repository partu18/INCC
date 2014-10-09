"use strict";

function EventsHandler() {
  this.initialize();
}

EventsHandler.prototype.initialize = function () {
  this.startTime = null;
  this.events = [];
  this.eventsID = [];
};

EventsHandler.prototype.addEvent = function (event, time) {
  this.events.push({event: event, time: time});
};

EventsHandler.prototype.start = function () {
  var i, length;
  function compareFunction(a, b) {
    if (b.time < a.time) {
      return 1;
    }
    if (b.time === a.time) {
      return 0;
    }
    return -1;
  }

  this.events.sort(compareFunction);
  length = this.events.length;

  for (i = 0; i < length; ++i) {

    this.eventsID.push(setTimeout(this.events[i].event, this.events[i].time));
  }
};

EventsHandler.prototype.stop = function () {
  var i, length;

  length = this.eventsID.length;

  for (i = 0; i < length; ++i) {

    clearTimeout(this.eventsID[i]);
  }
};