# VTK files

Drop `.vtp` (surface PolyData) files here.

Files in this directory are served at `/vtk/<filename>` on the site.

## Recommended workflow (OpenFOAM → web)

1. Run your OpenFOAM case
2. Open in ParaView → apply **Extract Surface** filter
3. **File → Save Data** → choose `.vtp` (XML PolyData)
4. Copy the `.vtp` file into this folder
5. Use the shortcode in any `.md` file:

```
{{</* vtk file="/vtk/yourfile.vtp" colorBy="p" title="My simulation" */>}}
```

## File size guidance

| Size      | Action                                      |
|-----------|---------------------------------------------|
| < 50 MB   | Commit normally                             |
| 50–100 MB | Use Git LFS: `git lfs track "*.vtp"`        |
| > 100 MB  | Host elsewhere and pass the full URL to `file=` |
