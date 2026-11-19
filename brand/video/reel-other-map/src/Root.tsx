import React from 'react';
import {Composition} from 'remotion';
import {Reel, TOTAL} from './Reel';
import '@fontsource/cormorant-garamond/500-italic.css';
import '@fontsource/cormorant-garamond/500.css';
import '@fontsource/lora/400.css';
import '@fontsource/shadows-into-light-two/400.css';

export const RemotionRoot: React.FC = () => (
  <Composition id="OtherMap" component={Reel} durationInFrames={TOTAL} fps={30} width={1080} height={1920} />
);
