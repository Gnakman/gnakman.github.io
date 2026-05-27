// Shim for vtk.js's static `import { create } from 'xmlbuilder2'`.
//
// jsDelivr's `xmlbuilder2@3.1.1/+esm` exposes only a `default` export, so
// vtk.js's `import { create }` fails to link ("does not provide an export named
// 'create'"). An import map remaps that dependency URL to this file. vtk.js
// actually CALLS create() (it builds an XML template at module-init), so this
// must provide a working create — not a stub.
//
// We pull the real xmlbuilder2 from esm.sh (a DIFFERENT URL, so the import map
// does not redirect it back into this shim) and re-export its create as a named
// export. esm.sh's xmlbuilder2 is self-contained (its own deps are inlined).
import * as xb2ns from "https://esm.sh/xmlbuilder2@3.1.1";

const xb2 = (xb2ns && xb2ns.default) ? xb2ns.default : xb2ns;

export const create =
  (typeof xb2ns.create === "function") ? xb2ns.create
  : (xb2 && typeof xb2.create === "function") ? xb2.create
  : function () { throw new Error("xmlbuilder2.create could not be resolved"); };

export default xb2;
