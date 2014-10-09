/*global Shape, EventsHandler*/
/*global MateMarote, stageWidth, stageHeight */
"use strict";

function buildObjectManifest(scope) {

  return {
    backdround: {
      constructor: Shape,
      addToStage: true,
      zIndex: 0,
      parameters: {
        src: "background",
        x: 0,
        y: 0
      }
    },
    circle: {
      constructor: Shape,
      addToStage: true,
      zIndex: 1,
      parameters: {
        src: "circle",
        visible: false,
        regX: 25,
        regY: 25,
        x: stageWidth * 0.5,
        y: stageHeight * 0.5,
        scaleX: 0.35,
        scaleY: 0.35
      }
    },
    leftArrow: {
      constructor: Shape,
      addToStage: true,
      zIndex: 1,
      parameters: {
        src: "arrow",
        visible: false,
        regX: 46,
        regY: 26,
        x: stageWidth * 0.5,
        y: stageHeight * 0.5,
        scaleX: 0.35,
        scaleY: 0.35
      }
    },
    rightArrow: {
      constructor: Shape,
      addToStage: true,
      zIndex: 1,
      parameters: {
        src: "arrow",
        visible: false,
        regX: 46,
        regY: 26,
        x: stageWidth * 0.5,
        y: stageHeight * 0.5,
        scaleX: -0.35,
        scaleY: 0.35
      }
    },
    line: {
      constructor: Shape,
      addToStage: true,
      zIndex: 1,
      parameters: {
        src: "line",
        visible: false,
        regX: 5,
        regY: 300,
        x: stageWidth * 0.5,
        y: stageHeight * 0.5,
        scaleX: 0.5,
        scaleY: 0.5
      }
    },
    events: {
      constructor: EventsHandler,
      addToStage: false,
      parameters: {

      }
    }
  };
}

var objectConstructors = {
  Shape: Shape,
  EventsHandler: EventsHandler
};