/*global createjs, setProperties*/
"use strict";

function Text(parameters) {
  this.initialize(parameters);
}

Text.prototype = new createjs.Text();
Text.prototype.textInitialize = Text.prototype.initialize;
Text.prototype.textTick = Text.prototype._tick;

Text.prototype.initialize = function (parameters) {
  // initian settings
  this.textInitialize(parameters.text, parameters.font, parameters.color);
  setProperties(this, parameters);
  var regCentered = parameters.hasOwnProperty("regCentered") ? parameters.regCentered : false;
  if (regCentered) {
    this.regY = this.getBounds().y + (this.getBounds().height * 0.5);
  }
};

Text.prototype.animation = function (parameters, time, interpolation) {
  return createjs.Tween.get(this)
    .to(parameters, time, interpolation);
};
