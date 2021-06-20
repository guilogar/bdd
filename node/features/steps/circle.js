'use strict';

const should = require('should');
const assert = require('assert');
const { Given, When, Then } = require('cucumber');
const { radiusArea } = require('../../src/circle-area');
const { NegativeRadius } = require('../../src/exceptions/negative-radius');

let globalRadius = 0;
Given('un radio de valor {float}', function (radius) {
  globalRadius = radius;
  assert(!isNaN(radius));
});

When('al calcular el area', function () {
  assert(true);
  return;
});

When('al calcular el area, lanza una exception de tipo NegativeRadius', function () {
  try {
    const area = radiusArea(globalRadius);
    assert(false);
  } catch (NegativeRadius) {
    assert(true);
  }
});
 
Then('el area es igual a ~{float} con un error absoluto menor que {float}', function (value, absoluteErrorLine) {
  const area = radiusArea(globalRadius);
  const absoluteError = Math.abs(area - value);
  assert(absoluteError < absoluteErrorLine);
});