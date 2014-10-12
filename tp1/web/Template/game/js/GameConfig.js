/*global stageWidth */
"use strict";

function buildGameConfig(/*mainScope*/) {
  return {
    paramName: "value",
    tappingTime: 30000,
    arrowTime: 30000,
    dualTime: 30000,
    fixationTime: 2000,
    currentTrial: "none",
    trial_000: JSON.stringify({
      type: "DA",
      hand: "R",
      arrowIntervalTime: 600,
      arrowDurationTime: 200,
      circleIntervalTime: 900,
      circleDurationTime: 200,
      leftArrow: {
        x: stageWidth * 0.5 - 50,
      },
      rightArrow: {
        x: stageWidth * 0.5 - 50,
      },
      circle: {
        x: stageWidth * 0.5 + 50,
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