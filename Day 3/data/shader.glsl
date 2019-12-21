#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

#define PROCESSING_TEXTURE_SHADER

uniform sampler2D texture;
uniform vec2 texOffset;

varying vec4 vertColor;
varying vec4 vertTexCoord;

void main(void) {
  // Grouping texcoord variables in order to make it work in the GMA 950. See post #13
  // in this thread:
  // http://www.idevgames.com/forums/thread-3467.html

  vec2 uv = vertTexCoord.xy;
  uv -= 0.5;

  float distanceToMid = length(uv.st);
  vec2 texOffsetNew = texOffset;

  texOffsetNew *= pow(distanceToMid*1.3, 4) * 1.2;

  vec2 tc0 = vertTexCoord.st + vec2(-texOffsetNew.s, -texOffsetNew.t);
  vec2 tc1 = vertTexCoord.st - vec2(-texOffsetNew.s, -texOffsetNew.t);
  vec2 tc2 = vertTexCoord.st + vec2(+texOffsetNew.s, -texOffsetNew.t);

  vec4 col = vec4(0);
  col.x = texture2D(texture, tc0).x;
  col.y = texture2D(texture, tc1).x;
  col.z = texture2D(texture, tc2).x;

  col = clamp(col, vec4(0.), vec4(0.5));
  col *= 2.;
  col.g *= 0.9;
  gl_FragColor = vec4(col) ;  
  // gl_FragColor.xy = uv.xy;
  // gl_FragColor.x = 0;
}
