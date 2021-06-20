'use strict';

const should = require('should');
const assert = require('assert');
const { Given, When, Then } = require('cucumber');
const { radiusArea } = require('../../src/circle-area.js');

let globalRadius = 0;
Given('un radio de valor {float}', function (radius) {
  globalRadius = radius;
  assert(radius > 0);
});

When('al calcular el area', function () {
  return;
});
 
Then('el area es igual a ~{float} con un error absoluto menor que {float}', function (value, absoluteErrorLine) {
  const area = radiusArea(globalRadius);
  const absoluteError = Math.abs(area - value);
  assert(absoluteError < absoluteErrorLine);
});