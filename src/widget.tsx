// Copyright (c) Clément Trassoudaine
// Distributed under the terms of the Modified BSD License.

import * as React from 'react';
import ReactDOM from 'react-dom';
import { DOMWidgetModel, DOMWidgetView, ISerializers } from '@jupyter-widgets/base';
import { Graph, GraphCanvas, GraphParameters } from 'tgraph';
import { MODULE_NAME, MODULE_VERSION } from './version';
import '../css/widget.css'



export
  class GraphModel extends DOMWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      _model_name: GraphModel.model_name,
      _model_module: GraphModel.model_module,
      _model_module_version: GraphModel.model_module_version,
      _view_name: GraphModel.view_name,
      _view_module: GraphModel.view_module,
      _view_module_version: GraphModel.view_module_version,
    };
  }

  static serializers: ISerializers = {
    ...DOMWidgetModel.serializers,
    // Add any extra serializers here
  }

  static model_name = 'GraphModel';
  static model_module = MODULE_NAME;
  static model_module_version = MODULE_VERSION;
  static view_name = 'GraphView';   // Set to null if no view
  static view_module = MODULE_NAME;   // Set to null if no view
  static view_module_version = MODULE_VERSION;
}

export
  class GraphView extends DOMWidgetView {
  render() {
    ReactDOM.render(<GraphCanvas graphData={new Graph(new Map(), [])} graphParams={new GraphParameters()} customMenuActions={new Map()} />, this.el);

    this.value_changed();
    this.model.on('change:value', this.value_changed, this);
  }

  value_changed() {
    this.model.get('value');
  }
}