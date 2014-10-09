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
      break;
    case "D":
      
      gameObjects.events.addEvent(show.bind(null, gameObjects.line),0);

      aparitionTimes = (gameData.tappingTime / currentConfig.circleIntervalTime);

      for (i = 0; i < aparitionTimes; ++i) {
        gameObjects.events.addEvent(show.bind(null, gameObjects.circle), i * currentConfig.circleIntervalTime);
        gameObjects.events.addEvent(hidden.bind(null, gameObjects.circle), (i * currentConfig.circleIntervalTime) + currentConfig.circleDurationTime);
      }

      aparitionTimes = (gameData.arrowTime / currentConfig.arrowIntervalTime);


      for (i = 0; i < aparitionTimes; i += 2) {
        gameObjects.events.addEvent(show.bind(null, gameObjects.leftArrow), i * currentConfig.arrowIntervalTime);
        gameObjects.events.addEvent(hidden.bind(null, gameObjects.leftArrow), (i * currentConfig.arrowIntervalTime) + currentConfig.arrowDurationTime);
      }

      for (i = 1; i < aparitionTimes; i += 2) {
        gameObjects.events.addEvent(show.bind(null, gameObjects.rightArrow), i * currentConfig.arrowIntervalTime);
        gameObjects.events.addEvent(hidden.bind(null, gameObjects.rightArrow), (i * currentConfig.arrowIntervalTime) + currentConfig.arrowDurationTime);
      }
      break;
    }

    addAllToSubStage(objectsManifest, currentConfig);
    stage.update();
    gameObjects.events.start();
  }

  function nextStep() {
  }

  function startGame() {
    var currentStatus;
    //createjs.Ticker.addEventListener("tick", stage);
    //createjs.Ticker.setFPS(60);

    // Default way to obtain the correct start point, it can be changed.
    currentStatus = Progress.progress.gameData.notFirstTime ? STATUS.RESUME_GAME : STATUS.DEPARTURE_POINT;
    currentConfig = Progress.getTrial(Progress.nextTrial(currentStatus));

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

    // used for the default way to obtain the correct start point, it can be changed.
    // if this default way isn't used this isn't necesary.
    if (status === STATUS.DEPARTURE_POINT) {

      Progress.progress.gameData.notFirstTime = true;
    }

    return "trial_000";
  };

  //////////////////////////////////////////////////////////////
  ////////// **** End game developer functions **** ////////////
  //////////////////////////////////////////////////////////////

  objectsManifest = gameInit(mainScope);
  //this is an aliasing to evoid writ the long name for the gameData
  gameData = MateMarote.gameData.stepConfig;

}());