/*global */
"use strict";

function buildGameConfig(/*mainScope*/) {
  return {
    paramName: "value",
    tappingTime: 30000,
    arrowTime: 30000,
    dualTime: 30000,
    fixationTime: 2000,
    currentTrial: "trial_000",
    trial_000: JSON.stringify({
      type: "D",
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
      }
    }),
    preload: JSON.stringify({
      background: "img/background.png",
      circle: "img/circle.png",
      arrow: "img/arrow.png",
      line: "img/line.png"
    })
  };
}