/*global Shape, EventsHandler, Text*/
/*global MateMarote, stageWidth, stageHeight, T_coverMessage, endMessage */
"use strict";

function buildObjectManifest(/*mainScope*/) {

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
    instructions: {
      constructor: Text,
      zIndex: 2,
      addToStage: true,
      parameters: {
        text: "a",
        font: "bold 36px Arial",
        color: "rgba(0,0,0,1)",
        regCentered: true,
        visible: false,
        scaleX: 0.5,
        scaleY: 0.5,
        x: 50,
        y: stageHeight * 0.5
      }
    },
    endText: {
      constructor: Text,
      zIndex: 2,
      addToStage: true,
      parameters: {
        text: endMessage,
        font: "bold 36px Arial",
        color: "rgba(0,0,0,1)",
        regCentered: true,
        visible: false,
        scaleX: 0.5,
        scaleY: 0.5,
        x: stageWidth * 0.5,
        y: stageHeight * 0.5
      }
    },
    image: {
      constructor: Shape,
      addToStage: true,
      zIndex: 2,
      parameters: {
        visible: false,
        scaleX: 0.5,
        scaleY: 0.5,
        x: 50,
        y: 300
      }
    },
    countDown: {
      constructor: Text,
      zIndex: 2,
      addToStage: true,
      parameters: {
        text: "3",
        font: "bold 36px Arial",
        color: "rgba(0,0,0,1)",
        regCentered: true,
        visible: false,
        scaleX: 2.5,
        scaleY: 2.5,
        x: stageWidth * 0.5,
        y: stageHeight * 0.5
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
  EventsHandler: EventsHandler,
  Text: Text,
};