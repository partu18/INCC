/*global buildGameConfig, buildObjectManifest, objectConstructors, gameObjects:true */
/*global MateMarote, Preloader, fromMobile, JSON, createjs */
/*global $, jQuery, stage:true, subStage:true, overStage:true, stageWidth:true, stageHeight:true, console */
/*exported buildObjects, addAllToSubStage, addMetrics, setProperties, gameInit */
"use strict";

function isTypeOf(obj, type) {
  var result = false;

  if (obj !== undefined) {

    result = obj.constructor.toString().indexOf(type) > -1;
  }
  return result;
}

function addAllToPreloader(preloadObj) {
  var iterator, start, end;

  $.each(preloadObj, function (key, value) {
    if (isTypeOf(value, "String")) {

      Preloader.add(key, value);
    } else {

      start     = value.indexes[0];
      end       = value.indexes[1];
      for (iterator = start; iterator <= end; ++iterator) {
        Preloader.add(key + iterator, value.prefix + iterator + value.extension);
      }
    }
  });
}

function dependenciesReady(dependencies) {
  var result = true;
  var numDependencies;
  var iterator;

  if (isTypeOf(dependencies, "Array")) {

    numDependencies = dependencies.length;
    for (iterator = 0; iterator < numDependencies; ++iterator) {

      if (!gameObjects.hasOwnProperty(dependencies[iterator])) {
        result = false;
      }
    }
  }

  return result;
}

function addAllToSubStage(objectsManifest, trialConfig) {
  var objectsList = [];
  var iterator;
  var cantObjects;
  var result;
  var wantTobeAdded;
  var compare = function (a, b) {

    // undefined zIndex are the biger positions
    if ((a.zIndex !== undefined) && (b.zIndex !== undefined)) {
      
      if (b.zIndex < a.zIndex) {
        result = 1;
      } else if (b.zIndex === a.zIndex) {
        result = 0;
      } else {
        result = -1;
      }

    } else if ((b.zIndex === undefined)) {
      result = -1;
    } else {
      result = 1;
    }

    return result;
  };

  trialConfig = trialConfig || {};

  $.each(objectsManifest, function (key, value) {

    wantTobeAdded = value.hasOwnProperty("addToStage") ? value.addToStage : true;
    if (wantTobeAdded) {
      objectsList.push({key: key, zIndex: value.zIndex});
    }
  });

  if (trialConfig.hasOwnProperty("trialObjects")) {

    $.each(trialConfig.trialObjects, function (key, value) {

      objectsList.push({key: key, zIndex: value.zIndex});
    });
  }

  objectsList.sort(compare);

  cantObjects = objectsList.length;
  for (iterator = 0; iterator < cantObjects; ++iterator) {
    subStage.addChild(gameObjects[objectsList[iterator].key]);
  }
}

function buildObjects(objectsManifest, trialConfig) {
  gameObjects = {};
  var queu = [];
  var key;
  var currentObject;
  var addSetting = function (tCKey, tCValue) {
    currentObject.parameters[tCKey] = tCValue;
  };

  trialConfig = trialConfig || {};
  // puting all objects in the queu of creation
  $.each(objectsManifest, function (key) {
    queu.push(key);
  });

  if (trialConfig.hasOwnProperty("trialObjects")) {
    $.each(trialConfig.trialObjects, function (key) {
      queu.push(key);
    });
  }

  // creating object
  while (queu.length > 0) {
    key = queu.shift();

    // searching the next objet to create
    if (objectsManifest.hasOwnProperty(key)) {

      currentObject = jQuery.extend(true, {}, objectsManifest[key]);
    } else if (trialConfig.trialObjects.hasOwnProperty(key)) {

      currentObject = jQuery.extend(true, {}, trialConfig.trialObjects[key]);
    }

    // if the object has all dependencies ready or hi hasn't dependencies the object is created
    // if there is some dependencies that need to be created before, the object isn't created and is returned to the queu whaiting for his dependencies
    if (dependenciesReady(currentObject.dependencies)) {

      if (trialConfig.hasOwnProperty(key)) {

        $.each(trialConfig[key], addSetting);
      }

      if (isTypeOf(currentObject.constructor, "String")) {

        gameObjects[key] = new objectConstructors[currentObject.constructor](currentObject.parameters);
      } else {

        gameObjects[key] = new currentObject.constructor(currentObject.parameters);
      }
    } else {
      console.log("Falta dependencias para " + key);
      queu.push(key);
    }
  }

  return gameObjects;
}

function setProperties(instance, parameters) {

  if (parameters !== undefined) {

    $.each(parameters, function (key, value) {
      instance[key] = value;
    });
  }
}

function gameInit(mainScope) {
  var mobile, firstNumber, secondNumber, jsonConfigData, preloadObj, gameConfig;


  MateMarote.init();
  stage = new createjs.Stage(mainScope.myCanvas);
  subStage = new createjs.Container();
  createjs.Touch.enable(stage);

  mobile = fromMobile();
  // Autoscaling procedure
  if (mobile) {

    stageWidth    = 800;
    stageHeight   = 450;
    firstNumber   = 9;
    secondNumber  = 16;
  } else {

    stageWidth    = 800;
    stageHeight   = 600;
    firstNumber   = 3;
    secondNumber  = 4;
  }

  subStage.scaleX = mainScope.myCanvas.width / stageWidth;
  subStage.scaleY = mainScope.myCanvas.height / stageHeight;

  if (subStage.scaleX < subStage.scaleY) {

    subStage.scaleY = subStage.scaleX;
    mainScope.myCanvas.height = (mainScope.myCanvas.width * firstNumber) / secondNumber;
  } else if (subStage.scaleX > subStage.scaleY) {

    subStage.scaleX = subStage.scaleY;
    mainScope.myCanvas.width  = (mainScope.myCanvas.height * secondNumber) / firstNumber;
  }

  overStage         = new createjs.Container();
  overStage.scaleX  = subStage.scaleX;
  overStage.scaleY  = subStage.scaleY;
  stage.addChild(overStage);
  stage.addChild(subStage);

  // creation of GC.
  var testModeGameConfig  = buildGameConfig(mainScope);

  // Sound is initialized here // ver que onda esto
  Preloader.init(stage, subStage);
  jsonConfigData = MateMarote.gameData;
  if (jsonConfigData === "TestMode") {
    console.log("Default config loaded.");
    gameConfig = testModeGameConfig;
  } else {
    gameConfig = jsonConfigData.stepConfig;
  }
  MateMarote.gameData = {};
  MateMarote.gameData.stepConfig = gameConfig;

  preloadObj = JSON.parse(gameConfig.preload);
  addAllToPreloader(preloadObj, gameConfig.preloadExtension);
  Preloader.start(mainScope.startGame);

  return buildObjectManifest(mainScope);
}