var tgraph = require('./index');
var base = require('@jupyter-widgets/base');

module.exports = {
  id: 'tgraph',
  requires: [base.IJupyterWidgetRegistry],
  activate: function(app, widgets) {
      widgets.registerWidget({
          name: 'tgraph',
          version: tgraph.version,
          exports: tgraph
      });
  },
  autoStart: true
};

