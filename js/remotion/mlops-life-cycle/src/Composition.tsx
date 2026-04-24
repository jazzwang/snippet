import { AbsoluteFill, Sequence, spring, useCurrentFrame, useVideoConfig, interpolate } from "remotion";
import React from 'react';

const TitleScreen: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const opacity = interpolate(frame, [0, 30, 50, 60], [0, 1, 1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const scale = spring({
    fps,
    frame,
    config: { damping: 12 },
  });

  return (
    <AbsoluteFill style={{ justifyContent: "center", alignItems: "center", backgroundColor: "#0b0f19", color: "white" }}>
      <h1 style={{ fontSize: 80, opacity, transform: `scale(${scale})`, textAlign: "center", fontFamily: "sans-serif" }}>
        The End-to-End<br/>MLOps Lifecycle
      </h1>
    </AbsoluteFill>
  );
};

const StageScene: React.FC<{ title: string; subtitle: string; color: string }> = ({ title, subtitle, color }) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  const titleOpacity = interpolate(frame, [0, 15], [0, 1], { extrapolateRight: "clamp" });
  const titleY = interpolate(frame, [0, 15], [50, 0], { extrapolateRight: "clamp" });

  const subtitleOpacity = interpolate(frame, [15, 30], [0, 1], { extrapolateRight: "clamp" });

  const bgWidth = spring({
    frame,
    fps,
    config: { damping: 100 },
  });

  const fadeOut = interpolate(frame, [durationInFrames - 15, durationInFrames], [1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });

  return (
    <AbsoluteFill style={{ backgroundColor: "#0b0f19", color: "white", padding: 80, display: "flex", flexDirection: "column", justifyContent: "center", opacity: fadeOut, fontFamily: "sans-serif" }}>
      <div style={{
        position: "absolute",
        left: 0,
        top: 0,
        bottom: 0,
        width: `${bgWidth * 100}%`,
        backgroundColor: color,
        opacity: 0.1,
      }} />
      <h2 style={{
        fontSize: 20,
        margin: 0,
        opacity: titleOpacity,
        transform: `translateY(${titleY}px)`,
        color: color
      }}>
        {title}
      </h2>
      <p style={{
        fontSize: 16,
        marginTop: 20,
        lineHeight: 1.5,
        opacity: subtitleOpacity,
        maxWidth: 1000
      }}>
        {subtitle}
      </p>
    </AbsoluteFill>
  );
};

export const MyComposition = () => {
  return (
    <AbsoluteFill style={{ backgroundColor: "#0b0f19" }}>
      <Sequence from={0} durationInFrames={50}>
        <TitleScreen />
      </Sequence>
      <Sequence from={50} durationInFrames={50}>
        <StageScene
          title="1. Data Engineering"
          subtitle="Extract, Transform, Load (ETL). Validating quality and engineering features for the ML model."
          color="#3b82f6"
        />
      </Sequence>
      <Sequence from={100} durationInFrames={50}>
        <StageScene
          title="2. Model Engineering"
          subtitle="Training algorithms, tuning hyperparameters, and tracking experiments with tools like MLflow."
          color="#8b5cf6"
        />
      </Sequence>
      <Sequence from={150} durationInFrames={50}>
        <StageScene
          title="3. CI/CD"
          subtitle="Automated testing, version control in a Model Registry, and containerizing via Docker."
          color="#10b981"
        />
      </Sequence>
      <Sequence from={200} durationInFrames={50}>
        <StageScene
          title="4. Model Deployment"
          subtitle="Taking models out of the lab into production for Batch, Real-time API, or Edge inference."
          color="#f59e0b"
        />
      </Sequence>
      <Sequence from={250} durationInFrames={50}>
        <StageScene
          title="5. Continuous Monitoring"
          subtitle="Watching for Data & Concept drift to automatically trigger Continuous Training (CT)."
          color="#ef4444"
        />
      </Sequence>
    </AbsoluteFill>
  );
};