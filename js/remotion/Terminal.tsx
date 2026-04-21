import React from "react";
import { useCurrentFrame, useVideoConfig, interpolate } from "remotion";

const TERMINAL_WIDTH = 1280;
const TERMINAL_HEIGHT = 1000;

const TYPEWRITER_TEXT = "npx skills add remotion-dev/skills";

const macOSLightTheme = {
  promptText: "#1a1a1a",
  commandText: "#0066cc",
  cursorBg: "#000000",
};

const TerminalWindow: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const charsToShow = interpolate(
    frame * fps,
    [0, TYPEWRITER_TEXT.length * 8],
    [0, TYPEWRITER_TEXT.length],
    {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    },
  );

  const typedText = TYPEWRITER_TEXT.slice(0, Math.floor(charsToShow));
  const isTypingComplete = charsToShow >= TYPEWRITER_TEXT.length;

  const cursorOpacity = isTypingComplete
    ? interpolate(frame % 40, [0, 20], [1, 0], {
        extrapolateLeft: "clamp",
        extrapolateRight: "clamp",
      })
    : 1;

  const terminalContentStyle: React.CSSProperties = {
    width: TERMINAL_WIDTH,
    height: TERMINAL_HEIGHT,
    backgroundColor: "transparent",
    fontFamily: "Menlo, Monaco, Consolas, monospace",
    fontSize: 48,
    lineHeight: 1.6,
    padding: 48,
    color: macOSLightTheme.promptText,
    position: "relative",
  };

  const cursorStyle: React.CSSProperties = {
    display: "inline-block",
    width: 28,
    height: 58,
    backgroundColor: macOSLightTheme.cursorBg,
    opacity: cursorOpacity,
    marginLeft: 2,
    verticalAlign: "text-bottom",
  };

  return (
    <div
      style={{
        width: TERMINAL_WIDTH,
        height: TERMINAL_HEIGHT,
        backgroundColor: "transparent",
        overflow: "hidden",
      }}
    >
      <div style={terminalContentStyle}>
        <div>
          <span style={{ color: macOSLightTheme.promptText }}>jazzw@</span>
          <span style={{ color: "#007aff" }}> ~ </span>
          <span>$ </span>
          <span style={{ color: macOSLightTheme.commandText }}>
            {typedText}
          </span>
          <span style={cursorStyle} />
        </div>
      </div>
    </div>
  );
};

export const Terminal = TerminalWindow;
