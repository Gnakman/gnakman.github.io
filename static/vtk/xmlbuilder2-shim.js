// Shim for vtk.js's static `import { create } from 'xmlbuilder2'`.
//
// vtk.js pulls in xmlbuilder2 only for its XML *writer* (vtkXMLWriter). This
// viewer only *reads* .vtp files — vtkXMLPolyDataReader parses XML with the
// browser's own parser, never xmlbuilder2 — so the writer path is dead code.
// But the static import must still resolve at link time, and jsDelivr's
// `xmlbuilder2@3.1.1/+esm` exposes only a `default` export (no named `create`),
// so `import { create }` throws "does not provide an export named 'create'".
//
// An import map remaps that dependency URL to this file. We only need to
// satisfy the link; create() simply throws if XML *writing* is ever attempted.
export function create() {
  throw new Error('xmlbuilder2.create is unavailable in this build (XML writing is not supported)');
}
export default { create };
