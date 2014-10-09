/*global createjs, Preloader, setProperties*/
"use strict";

function Shape(parameters) {
  this.initialize(parameters);
}

Shape.prototype = new createjs.Bitmap();
Shape.prototype.BitmapInitialize = Shape.prototype.initialize;
Shape.prototype.BitmapTick = Shape.prototype._tick;

Shape.prototype.initialize = function (parameters) {
  this.BitmapInitialize(Preloader.get(parameters.src));
  setProperties(this, parameters);

  var regCentered = parameters.hasOwnProperty("regCentered") ? parameters.regCentered : false;
  if (regCentered) {
    this.regX = this.image.width * 0.5;
    this.regY = this.image.height * 0.5;
  }
};

Shape.prototype.animation = function (parameters, time, interpolation) {
  return createjs.Tween.get(this)
    .to(parameters, time, interpolation);
};

Shape.prototype.fadeOut = function (time) {
  return createjs.Tween.get(this)
    .to({alpha: 0}, time, createjs.Ease.out);
};