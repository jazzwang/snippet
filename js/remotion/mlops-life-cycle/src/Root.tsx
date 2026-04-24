import "./index.css";
import { Composition } from "remotion";
import { MyComposition } from "./Composition";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="MLOps"
        component={MyComposition}
        durationInFrames={300}
        fps={10}
        width={640}
        height={256}
      />
    </>
  );
};
