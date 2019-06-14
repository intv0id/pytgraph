// Copyright (c) Clément Trassoudaine
// Distributed under the terms of the Modified BSD License.

import {
  DOMWidgetModel, DOMWidgetView, ISerializers
} from '@jupyter-widgets/base';

import {
  MODULE_NAME, MODULE_VERSION
} from './version';

import { GraphView, Graph, GraphOptions } from "tgraph";
import { GraphSerializer } from "./graphSerializer";


export
class tgraphModel extends DOMWidgetModel {
  _model_name =  tgraphModel.model_name;
  _model_module =  tgraphModel.model_module;
  _model_module_version = tgraphModel.model_module_version;
  _view_name = tgraphModel.view_name;
  _view_module = tgraphModel.view_module;
  _view_module_version = tgraphModel.view_module_version;
  graph: Graph = new Graph();
  graphOptions: GraphOptions = new GraphOptions();

  static serializers: ISerializers = {
      ...DOMWidgetModel.serializers,
      "Graph": GraphSerializer,
    }

  static model_name = 'tgraphModel';
  static model_module = MODULE_NAME;
  static model_module_version = MODULE_VERSION;
  static view_name = 'tgraphView';
  static view_module = MODULE_NAME;
  static view_module_version = MODULE_VERSION;
}


export class tgraphView extends DOMWidgetView {
  render() {
    this.value_changed();
    this.model.on("change:graph", this.value_changed, this);
  }

  value_changed() {
    let gv = new GraphView(this.el, this.model.get('graphOptions'))
    gv.draw(this.model.get('graph'))
  }
}
