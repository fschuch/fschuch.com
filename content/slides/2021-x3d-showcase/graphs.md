```mermaid
flowchart LR
    subgraph x3d[XCompact3d]
        Initialization --> sb
        sb[module sandbox] --> ml[Main Loop & Finalize]
    end
    D[(Disk)] -->|Parameters file| Initialization
    D -->|"Data Arrays"| sb
    subgraph et["External tool"]
        SL["Initial Condition\nBoundary Conditions\nGeometry (IBM)\nOthers"]
    end
    SL --> D
```

```json
{
  "theme": "base",
  "themeVariables": {
    "fontFamily": "arial",
    "fontSize": "20px"
  }
}
```