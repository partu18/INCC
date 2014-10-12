/*global stageWidth, coverMessage */
"use strict";

function buildGameConfig(/*mainScope*/) {
  return {
    continueKey: 13,
    startKey: 13,
    tappingTime: 30000,
    arrowTime: 30000,
    dualTime: 30000,
    fixationTime: 2000,
    currentTrial: "none",
    trial_000: JSON.stringify({
      message: {
        text: coverMessage
      }
    }),
    trial_001: JSON.stringify({
      type: "D",
      hand: "R",
      arrowIntervalTime: 600,
      arrowDurationTime: 200,
      circleIntervalTime: 900,
      circleDurationTime: 200,
      message: {
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
      imgMessage: {
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