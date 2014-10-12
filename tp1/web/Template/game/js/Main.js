"use strict";
/*global gameInit, buildObjects, MateMarote, Progress, addAllToSubStage */
/*global STATUS, gameObjects, stage, $, window */
/*exported instructionsMessage, coverMessage */
/*global instructionsMessage, finishTrial, coverMessage */
(function () {
  var currentConfig;
  var objectsManifest;
  var gameData;

  var coverKey        = false;
  var presentationKey = false;
  var instructionsKey = false;

  var myCanvas = $("#stageCanvas").get(0);

  ///////////////////////////////////////////////////////////////
  /////////////////// **** Functions **** ///////////////////////
  ///////////////////////////////////////////////////////////////

  function finishGame() {

    Progress.gameEnded();
  }

  function nextStep() {
    currentConfig = Progress.getTrial(Progress.nextTrial());

    if (currentConfig !== undefined) {
      buildObjects(objectsManifest, currentConfig);
      addAllToSubStage(objectsManifest, currentConfig);
      console.log(gameObjects);
      instructionsMessage();
    } else {
      finishTrial();
    }
  }

  function finishTrial() {
    nextStep();
  }

  function playTrial() {
    var i, aparitionTimes;

    function show(object) {
      object.visible = true;
      stage.update();
    }

    function hidden(object) {
      object.visible = false;
      stage.update();
    }

    function setCountDown(object, number) {

      object.text = number.toString();
      object.visible = true;
      stage.update();
    }


    // seteando la cuenta regresiva

    for (i = 0; i < 4; ++i) {
      gameObjects.events.addEvent(setCountDown.bind(null, gameObjects.countDown, i), (3 - i) * 1000);
    }

    gameObjects.events.addEvent(hidden.bind(null, gameObjects.countDown), 4000);

    // seteando las apariciones correctas
    switch (currentConfig.type) {
    case "T":
      aparitionTimes = (gameData.tappingTime / currentConfig.circleIntervalTime);

      for (i = 0; i < aparitionTimes; ++i) {
        gameObjects.events.addEvent(show.bind(null, gameObjects.circle), 4500 + i * currentConfig.circleIntervalTime);
        gameObjects.events.addEvent(hidden.bind(null, gameObjects.circle), 4500 + (i * currentConfig.circleIntervalTime) + currentConfig.circleDurationTime);
      }

      gameObjects.events.addEvent(show.bind(null, gameObjects.endText),  4500 +  currentConfig.tappingTime);
      gameObjects.events.addEvent(hidden.bind(null, gameObjects.endText),  4500 +  currentConfig.tappingTime + currentConfig.fixationTime);
      gameObjects.events.addEvent(finishTrial,  4500 +  currentConfig.tappingTime + currentConfig.fixationTime);
      break;
    case "A":
      aparitionTimes = (gameData.arrowTime / currentConfig.arrowIntervalTime);


      for (i = 0; i < aparitionTimes; i += 2) {
        gameObjects.events.addEvent(show.bind(null, gameObjects.leftArrow), 4500 +  i * currentConfig.arrowIntervalTime);
        gameObjects.events.addEvent(hidden.bind(null, gameObjects.leftArrow), 4500 + (i * currentConfig.arrowIntervalTime) + currentConfig.arrowDurationTime);
      }

      for (i = 1; i < aparitionTimes; i += 2) {
        gameObjects.events.addEvent(show.bind(null, gameObjects.rightArrow), 4500 + i * currentConfig.arrowIntervalTime);
        gameObjects.events.addEvent(hidden.bind(null, gameObjects.rightArrow), 4500 + (i * currentConfig.arrowIntervalTime) + currentConfig.arrowDurationTime);
      }

      gameObjects.events.addEvent(show.bind(null, gameObjects.endText),  4500 +  currentConfig.tappingTime);
      gameObjects.events.addEvent(hidden.bind(null, gameObjects.endText),  4500 +  currentConfig.tappingTime + currentConfig.fixationTime);
      gameObjects.events.addEvent(finishTrial, 4500 + currentConfig.arrowTime + currentConfig.fixationTime);
      break;
    case "D":

      gameObjects.events.addEvent(show.bind(null, gameObjects.line), 4500);

      aparitionTimes = (gameData.dualTime / currentConfig.circleIntervalTime);

      for (i = 0; i < aparitionTimes; ++i) {
        gameObjects.events.addEvent(show.bind(null, gameObjects.circle), 4500 + i * currentConfig.circleIntervalTime);
        gameObjects.events.addEvent(hidden.bind(null, gameObjects.circle), 4500 + (i * currentConfig.circleIntervalTime) + currentConfig.circleDurationTime);
      }

      aparitionTimes = (gameData.dualTime / currentConfig.arrowIntervalTime);


      for (i = 0; i < aparitionTimes; i += 2) {
        gameObjects.events.addEvent(show.bind(null, gameObjects.leftArrow), 4500 + i * currentConfig.arrowIntervalTime);
        gameObjects.events.addEvent(hidden.bind(null, gameObjects.leftArrow), 4500 + (i * currentConfig.arrowIntervalTime) + currentConfig.arrowDurationTime);
      }

      for (i = 1; i < aparitionTimes; i += 2) {
        gameObjects.events.addEvent(show.bind(null, gameObjects.rightArrow), 4500 + i * currentConfig.arrowIntervalTime);
        gameObjects.events.addEvent(hidden.bind(null, gameObjects.rightArrow), 4500 + (i * currentConfig.arrowIntervalTime) + currentConfig.arrowDurationTime);
      }

      gameObjects.events.addEvent(show.bind(null, gameObjects.endText),  4500 +  currentConfig.tappingTime);
      gameObjects.events.addEvent(hidden.bind(null, gameObjects.endText),  4500 +  currentConfig.tappingTime + currentConfig.fixationTime);
      gameObjects.events.addEvent(finishTrial.bind(null), 4500 + gameData.dualTime + gameData.fixationTime);
      break;
    }

    //console.log(4500, gameData.dualTime, gameData.fixationTime);

    stage.update();
    gameObjects.events.start();
  }

  function startGame() {

    currentConfig = Progress.getTrial(Progress.nextTrial());
    buildObjects(objectsManifest, currentConfig);
    addAllToSubStage(objectsManifest, currentConfig);

    coverMessage();
  }

  var mainScope = {
    myCanvas: myCanvas,
    startGame: startGame,
    finishTrial: finishTrial,
    nextStep: nextStep,
    playTrial: playTrial,
    finishGame: finishGame
  };

  ///////////////////////////////////////////////////////////////
  //////////////// **** End of Functions **** ///////////////////
  ///////////////////////////////////////////////////////////////



  //////////////////////////////////////////////////////////////
  //////////// **** Game developer functions **** //////////////
  //////////////////////////////////////////////////////////////

  function coverMessage() {

    gameObjects.cover.visible = true;
    stage.update();
    setTimeout(function () { coverKey = true; }, 250);
  }

  function presentationMessage() {

    gameObjects.presentation.visible = true;
    stage.update();
    setTimeout(function () { presentationKey = true; }, 250);
  }

  function instructionsMessage() {

    gameObjects.instructions.visible = true;
    gameObjects.image.visible = true;
    stage.update();
    setTimeout(function () { instructionsKey = true; }, 250);
  }

  Progress.nextTrial = function () {
    var i;
    var trials = ["none", "trial_000", "trial_001", "trial_002", "trial_003"];
    var result = null;
    var length = trials.length;

    for (i = 0; i < (length - 1); ++i) {

      if (gameData.currentTrial === trials[i]) {
        result = trials[i + 1];
        break;
      }
    }

    gameData.currentTrial = result;

    return result;
  };

  $(window).keydown(function (e) {
    var itsCoverKey         = (e.keyCode === gameData.coverKey);
    var itsPresentationKey  = (e.keyCode === gameData.presentationsKey);
    var itsInstructionsKey  = (e.keyCode === gameData.instructionsKey);

    if (coverKey && itsCoverKey) {

      coverKey = false;
      gameObjects.cover.visible = false;
      presentationMessage();
    }

    if (presentationKey && itsPresentationKey) {

      presentationKey = false;
      gameObjects.presentation.visible = false;
      nextStep();
    }

    if (instructionsKey && itsInstructionsKey) {

      instructionsKey = false;
      gameObjects.instructions.visible = false;
      gameObjects.image.visible = false;
      playTrial();
    }
  });

  //////////////////////////////////////////////////////////////
  ////////// **** End game developer functions **** ////////////
  //////////////////////////////////////////////////////////////

  objectsManifest = gameInit(mainScope);
  gameData        = MateMarote.gameData.stepConfig;

}());