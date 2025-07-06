import React, { useState } from "react";

const GRID_WIDTH = 5;
const GRID_HEIGHT = 10;
const CELL_SIZE = 100; // in pixels

export default function SensorGrid() {
  const [viewTransform, setViewTransform] = useState({ x: 0, y: 0, scale: 1 });

  const handleCellClick = (x, y) => {
    const targetScale = 2;
    const offsetX = x * CELL_SIZE * targetScale - window.innerWidth / 2 + (CELL_SIZE * targetScale) / 2;
    const offsetY = y * CELL_SIZE * targetScale - window.innerHeight / 2 + (CELL_SIZE * targetScale) / 2;

    setViewTransform({ x: -offsetX, y: -offsetY, scale: targetScale });
  };

  const resetView = () => setViewTransform({ x: 0, y: 0, scale: 1 });

  return (
    <div className="w-screen h-screen overflow-hidden relative bg-gray-100">
      <button
        onClick={resetView}
        className="absolute top-4 left-4 z-10 bg-white px-4 py-2 shadow rounded"
      >
        Reset View
      </button>

      <svg
        width={GRID_WIDTH * CELL_SIZE}
        height={GRID_HEIGHT * CELL_SIZE}
        className="absolute top-0 left-0"
        style={{
          transform: `translate(${viewTransform.x}px, ${viewTransform.y}px) scale(${viewTransform.scale})`,
          transformOrigin: "top left",
          transition: "transform 0.5s ease"
        }}
      >
        {/* Grid Cells */}
        {[...Array(GRID_HEIGHT)].map((_, row) =>
          [...Array(GRID_WIDTH)].map((_, col) => (
            <rect
              key={`cell-${col}-${row}`}
              x={col * CELL_SIZE}
              y={row * CELL_SIZE}
              width={CELL_SIZE}
              height={CELL_SIZE}
              fill="white"
              stroke="gray"
              onClick={() => handleCellClick(col, row)}
              className="cursor-pointer"
            />
          ))
        )}

        {/* Overlapping Colored Shapes */}
        <circle cx={150} cy={150} r={40} fill="rgba(255,0,0,0.6)" />
        <rect x={200} y={250} width={100} height={60} fill="rgba(0,128,255,0.5)" />
        <polygon
          points="400,700 450,650 500,700"
          fill="rgba(0,200,0,0.6)"
        />
      </svg>
    </div>
  );
}
