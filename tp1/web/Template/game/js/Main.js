"use strict";
/*global gameInit, buildObjects, MateMarote, Progress, addAllToSubStage */
/*global STATUS, gameObjects, stage, $ */


(function () {
  var currentConfig;
  var objectsManifest;
  var gameData;
  var myCanvas = $("#stageCanvas").get(0);


  ///////////////////////////////////////////////////////////////
  /////////////////// **** Functions **** ///////////////////////
  ///////////////////////////////////////////////////////////////

  function finishGame() {

    Progress.gameEnded();
    MateMarote.synchronize();
  }

  function finishTrial(status) {
  }

  function nextStep() {
  }

  function playTrial() {
    var i, aparitionTimes;
    Progress.trialPlay();

    function show(object) {
      object.visible = true;
      stage.update();
    }

    function hidden(object) {
      object.visible = false;
      stage.update();
    }


    buildObjects(objectsManifest, currentConfig);

    switch (currentConfig.type) {
    case "T":
      aparitionTimes = (gameData.tappingTime / currentConfig.circleIntervalTime);

      for (i = 0; i < aparitionTimes; ++i) {
        gameObjects.events.addEvent(show.bind(null, gameObjects.circle), i * currentConfig.circleIntervalTime);
        gameObjects.events.addEvent(hidden.bind(null, gameObjects.circle), (i * currentConfig.circleIntervalTime) + currentConfig.circleDurationTime);
      }

      gameObjects.events.addEvent(nextStep, currentConfig.tappingTime + currentConfig.fixationTime);
      break;
    case "A":
      aparitionTimes = (gameData.arrowTime / currentConfig.arrowIntervalTime);


      for (i = 0; i < aparitionTimes; i += 2) {
        gameObjects.events.addEvent(show.bind(null, gameObjects.leftArrow), i * currentConfig.arrowIntervalTime);
        gameObjects.events.addEvent(hidden.bind(null, gameObjects.leftArrow), (i * currentConfig.arrowIntervalTime) + currentConfig.arrowDurationTime);
      }

      for (i = 1; i < aparitionTimes; i += 2) {
        gameObjects.events.addEvent(show.bind(null, gameObjects.rightArrow), i * currentConfig.arrowIntervalTime);
        gameObjects.events.addEvent(hidden.bind(null, gameObjects.rightArrow), (i * currentConfig.arrowIntervalTime) + currentConfig.arrowDurationTime);
      }

      gameObjects.events.addEvent(nextStep, currentConfig.arrowTime + currentConfig.fixationTime);
      break;
    case "D":

      gameObjects.events.addEvent(show.bind(null, gameObjects.line), 0);

      aparitionTimes = (gameData.dualTime / currentConfig.circleIntervalTime);

      for (i = 0; i < aparitionTimes; ++i) {
        gameObjects.events.addEvent(show.bind(null, gameObjects.circle), i * currentConfig.circleIntervalTime);
        gameObjects.events.addEvent(hidden.bind(null, gameObjects.circle), (i * currentConfig.circleIntervalTime) + currentConfig.circleDurationTime);
      }

      aparitionTimes = (gameData.dualTime / currentConfig.arrowIntervalTime);


      for (i = 0; i < aparitionTimes; i += 2) {
        gameObjects.events.addEvent(show.bind(null, gameObjects.leftArrow), i * currentConfig.arrowIntervalTime);
        gameObjects.events.addEvent(hidden.bind(null, gameObjects.leftArrow), (i * currentConfig.arrowIntervalTime) + currentConfig.arrowDurationTime);
      }

      for (i = 1; i < aparitionTimes; i += 2) {
        gameObjects.events.addEvent(show.bind(null, gameObjects.rightArrow), i * currentConfig.arrowIntervalTime);
        gameObjects.events.addEvent(hidden.bind(null, gameObjects.rightArrow), (i * currentConfig.arrowIntervalTime) + currentConfig.arrowDurationTime);
      }

      gameObjects.events.addEvent(nextStep, gameData.dualTime + currentConfig.fixationTime);
      break;
    }


    addAllToSubStage(objectsManifest, currentConfig);
    stage.update();
    gameObjects.events.start();
  }

  function startGame() {
    var currentStatus;
    currentConfig = Progress.getTrial(Progress.nextTrial(STATUS.DEPARTURE_POINT));

    playTrial();
  }

  var mainScope = {
    myCanvas: myCanvas,
    startGame: startGame,
    finishTrial: finishTrial,
    nextStep: nextStep,
    playTrial: playTrial,
    finishGame: finishGame
    // Here it be defined more objects. This is the comunication way with the whole template environment
  };

  ///////////////////////////////////////////////////////////////
  //////////////// **** End of Functions **** ///////////////////
  ///////////////////////////////////////////////////////////////



  //////////////////////////////////////////////////////////////
  //////////// **** Game developer functions **** //////////////
  //////////////////////////////////////////////////////////////


  Progress.nextTrial = function (status) {
    var i;
    var trials = ["none", "trial_000", "trial_001", "trial_002", "trial_003"];
    var result = null;
    var length = trials.length;

    for (i = 0; i < (length - 1); ++i) {

      if (gameData.currentTrial === trials[i]) {
        result = trials[i + 1];
      }
    }

    return result;
  };



  //////////////////////////////////////////////////////////////
  ////////// **** End game developer functions **** ////////////
  //////////////////////////////////////////////////////////////

  objectsManifest = gameInit(mainScope);
  //this is an aliasing to evoid writ the long name for the gameData
  gameData = MateMarote.gameData.stepConfig;

}());