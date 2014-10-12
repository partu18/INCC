/*global Text, Shape, EventHandler */
/*global stageWidth, stageHeight, */
/*global T_coverMessage, presentationMessage, message1 */
"use strict";

function buildGameConfig(/*mainScope*/) {
  return {
    coverKey: 13,
    presentationsKey: 13,
    instructionsKey: 13,
    tappingTime: 30000,
    arrowTime: 30000,
    dualTime: 30000,
    fixationTime: 2000,
    currentTrial: "none",
    trial_000: JSON.stringify({
      trialObjects: {
        cover: {
          constructor: "Text",
          zIndex: 2,
          addToStage: true,
          parameters: {
            text: T_coverMessage,
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
        presentation: {
          constructor: "Text",
          zIndex: 2,
          addToStage: true,
          parameters: {
            text: presentationMessage,
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
      }
    }),
    trial_001: JSON.stringify({
      type: "D",
      hand: "R",
      arrowIntervalTime: 600,
      arrowDurationTime: 200,
      circleIntervalTime: 900,
      circleDurationTime: 200,
      instructions: {
        text: message1
      },
      leftArrow: {
        x: stageWidth * 0.5 - 50,
        visible: false
      },
      rightArrow: {
        x: stageWidth * 0.5 - 50,
        visible: false
      },
      circle: {
        x: stageWidth * 0.5 + 50,
        visible: false
      },
      image: {
        src: "enter"
      }
    }),
    trial_002: JSON.stringify({
      type: "D",
      hand: "R",
      arrowIntervalTime: 600,
      arrowDurationTime: 200,
      circleIntervalTime: 900,
      circleDurationTime: 200,
      instructions: {
        text: message1
      },
      leftArrow: {
        x: stageWidth * 0.5 - 50,
        visible: false
      },
      rightArrow: {
        x: stageWidth * 0.5 - 50,
        visible: false
      },
      circle: {
        x: stageWidth * 0.5 + 50,
        visible: false
      },
      image: {
        src: "enter"
      }
    }),
    preload: JSON.stringify({
      background: "img/background.png",
      circle: "img/circle.png",
      arrow: "img/arrow.png",
      line: "img/line.png",
      enter: "img/enter.jpg"
    })
  };
}