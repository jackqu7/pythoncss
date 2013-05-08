this code

  from parse import Style, Mixin

  class BorderRadius(Mixin):
      def _border_radius(self):
          return '%ipx' % self.Meta.border_radius_size

      @property
      def border_radius(self):
          return self._border_radius()

      @property
      def _webkit_border_radius(self):
          return self._border_radius()

      @property
      def _moz_border_radius(self):
          return self._border_radius()


  class Body(Style):
      @property
      def font_family(self):
          import random
          return random.choice(['helvetica', 'comic sans ms'])


  class MakeDivsRed(Style, BorderRadius):
      class Meta:
          target = 'div'    
          border_radius_size = 5

      background_color = 'red'
      color = 'blue'
      width = 95


produces this css

  body {
  	font-family: helvetica;
  }
  div {
  	-moz-border-radius: 5px;
  	-webkit-border-radius: 5px;
  	background-color: red;
  	border-radius: 5px;
  	color: blue;
  	width: 95px;
  }
  