# Scheduling block audit (``apply_rule`` chains)

Read-only AST scan of **ordered** ``apply_rule("x.y.z", …)`` calls.  Strings that are not the first argument to ``apply_rule`` are ignored.

- **scanned_py_files**: `20`
- **duplicate_cross_file_groups**: `75`

## Duplicate groups (longest first)

### 1 — `1685e23755e3` (10 sūtras)

```
1.1.3 → 1.1.7 → 1.1.8 → 1.1.9 → 1.1.10 → 1.1.11 → 1.1.12 → 1.1.13 → 1.1.14 → 1.1.100
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 279–291 |
| `pipelines/krdanta.py` | `__module__` | 150–160 |
| `pipelines/krdanta.py` | `__module__` | 225–235 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 2 — `d77483ce8421` (10 sūtras)

```
4.1.2 → 1.3.2 → 1.3.3 → 1.3.4 → 1.3.5 → 1.3.6 → 1.3.7 → 1.3.8 → 1.3.9 → 1.3.10
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 97–106 |
| `pipelines/subanta_trc.py` | `__module__` | 58–68 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 3 — `c53f79f06948` (9 sūtras)

```
1.1.3 → 1.1.7 → 1.1.8 → 1.1.9 → 1.1.10 → 1.1.11 → 1.1.12 → 1.1.13 → 1.1.14
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 279–289 |
| `pipelines/krdanta.py` | `__module__` | 150–159 |
| `pipelines/krdanta.py` | `__module__` | 225–234 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 4 — `e8d1ade0ebb3` (9 sūtras)

```
1.1.7 → 1.1.8 → 1.1.9 → 1.1.10 → 1.1.11 → 1.1.12 → 1.1.13 → 1.1.14 → 1.1.100
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 280–291 |
| `pipelines/krdanta.py` | `__module__` | 151–160 |
| `pipelines/krdanta.py` | `__module__` | 226–235 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 5 — `377883e69df5` (9 sūtras)

```
4.1.2 → 1.3.2 → 1.3.3 → 1.3.4 → 1.3.5 → 1.3.6 → 1.3.7 → 1.3.8 → 1.3.9
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 97–105 |
| `pipelines/subanta_trc.py` | `__module__` | 58–67 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 6 — `d448e8fccbea` (9 sūtras)

```
1.3.2 → 1.3.3 → 1.3.4 → 1.3.5 → 1.3.6 → 1.3.7 → 1.3.8 → 1.3.9 → 1.3.10
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 98–106 |
| `pipelines/subanta_trc.py` | `__module__` | 60–68 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 7 — `2324e25a60db` (8 sūtras)

```
1.1.8 → 1.1.9 → 1.1.10 → 1.1.11 → 1.1.12 → 1.1.13 → 1.1.14 → 1.1.100
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 283–291 |
| `pipelines/krdanta.py` | `__module__` | 153–160 |
| `pipelines/krdanta.py` | `__module__` | 228–235 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 8 — `5c7e7e04b31b` (8 sūtras)

```
1.1.3 → 1.1.7 → 1.1.8 → 1.1.9 → 1.1.10 → 1.1.11 → 1.1.12 → 1.1.13
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 279–288 |
| `pipelines/krdanta.py` | `__module__` | 150–158 |
| `pipelines/krdanta.py` | `__module__` | 225–233 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 9 — `cc877fcc4014` (8 sūtras)

```
1.1.7 → 1.1.8 → 1.1.9 → 1.1.10 → 1.1.11 → 1.1.12 → 1.1.13 → 1.1.14
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 280–289 |
| `pipelines/krdanta.py` | `__module__` | 151–159 |
| `pipelines/krdanta.py` | `__module__` | 226–234 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 10 — `1ebe1e3f845d` (8 sūtras)

```
4.1.2 → 1.3.2 → 1.3.3 → 1.3.4 → 1.3.5 → 1.3.6 → 1.3.7 → 1.3.8
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 97–104 |
| `pipelines/subanta_trc.py` | `__module__` | 58–66 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 11 — `2684f2bc3891` (8 sūtras)

```
1.3.3 → 1.3.4 → 1.3.5 → 1.3.6 → 1.3.7 → 1.3.8 → 1.3.9 → 1.3.10
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 99–106 |
| `pipelines/subanta_trc.py` | `__module__` | 61–68 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 12 — `c4820671bdd5` (8 sūtras)

```
1.3.2 → 1.3.3 → 1.3.4 → 1.3.5 → 1.3.6 → 1.3.7 → 1.3.8 → 1.3.9
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 98–105 |
| `pipelines/subanta_trc.py` | `__module__` | 60–67 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 13 — `bd55a1d14759` (7 sūtras)

```
1.1.8 → 1.1.9 → 1.1.10 → 1.1.11 → 1.1.12 → 1.1.13 → 1.1.14
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 283–289 |
| `pipelines/krdanta.py` | `__module__` | 153–159 |
| `pipelines/krdanta.py` | `__module__` | 228–234 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 14 — `c46ea4bd90b9` (7 sūtras)

```
1.1.7 → 1.1.8 → 1.1.9 → 1.1.10 → 1.1.11 → 1.1.12 → 1.1.13
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 280–288 |
| `pipelines/krdanta.py` | `__module__` | 151–158 |
| `pipelines/krdanta.py` | `__module__` | 226–233 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 15 — `ccab506c611c` (7 sūtras)

```
1.1.9 → 1.1.10 → 1.1.11 → 1.1.12 → 1.1.13 → 1.1.14 → 1.1.100
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 284–291 |
| `pipelines/krdanta.py` | `__module__` | 154–160 |
| `pipelines/krdanta.py` | `__module__` | 229–235 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 16 — `ef2f7612b6bb` (7 sūtras)

```
1.1.3 → 1.1.7 → 1.1.8 → 1.1.9 → 1.1.10 → 1.1.11 → 1.1.12
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 279–287 |
| `pipelines/krdanta.py` | `__module__` | 150–157 |
| `pipelines/krdanta.py` | `__module__` | 225–232 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 17 — `049307f22e75` (7 sūtras)

```
1.3.2 → 1.3.3 → 1.3.4 → 1.3.5 → 1.3.6 → 1.3.7 → 1.3.8
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 98–104 |
| `pipelines/subanta_trc.py` | `__module__` | 60–66 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 18 — `3e4f30abd4f9` (7 sūtras)

```
4.1.2 → 1.3.2 → 1.3.3 → 1.3.4 → 1.3.5 → 1.3.6 → 1.3.7
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 97–103 |
| `pipelines/subanta_trc.py` | `__module__` | 58–65 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 19 — `90a7fb70876e` (7 sūtras)

```
1.3.3 → 1.3.4 → 1.3.5 → 1.3.6 → 1.3.7 → 1.3.8 → 1.3.9
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 99–105 |
| `pipelines/subanta_trc.py` | `__module__` | 61–67 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 20 — `98981d7d2b98` (7 sūtras)

```
1.3.4 → 1.3.5 → 1.3.6 → 1.3.7 → 1.3.8 → 1.3.9 → 1.3.10
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 100–106 |
| `pipelines/subanta_trc.py` | `__module__` | 62–68 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 21 — `268a17a0bf60` (6 sūtras)

```
1.1.3 → 1.1.7 → 1.1.8 → 1.1.9 → 1.1.10 → 1.1.11
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 279–286 |
| `pipelines/krdanta.py` | `__module__` | 150–156 |
| `pipelines/krdanta.py` | `__module__` | 225–231 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 22 — `8726d9b675f2` (6 sūtras)

```
1.1.7 → 1.1.8 → 1.1.9 → 1.1.10 → 1.1.11 → 1.1.12
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 280–287 |
| `pipelines/krdanta.py` | `__module__` | 151–157 |
| `pipelines/krdanta.py` | `__module__` | 226–232 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 23 — `b6cd59d5dc70` (6 sūtras)

```
1.1.10 → 1.1.11 → 1.1.12 → 1.1.13 → 1.1.14 → 1.1.100
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 285–291 |
| `pipelines/krdanta.py` | `__module__` | 155–160 |
| `pipelines/krdanta.py` | `__module__` | 230–235 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 24 — `e12b97f275bb` (6 sūtras)

```
1.1.9 → 1.1.10 → 1.1.11 → 1.1.12 → 1.1.13 → 1.1.14
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 284–289 |
| `pipelines/krdanta.py` | `__module__` | 154–159 |
| `pipelines/krdanta.py` | `__module__` | 229–234 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 25 — `f34b08ea02bf` (6 sūtras)

```
1.1.8 → 1.1.9 → 1.1.10 → 1.1.11 → 1.1.12 → 1.1.13
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 283–288 |
| `pipelines/krdanta.py` | `__module__` | 153–158 |
| `pipelines/krdanta.py` | `__module__` | 228–233 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 26 — `298fec72950a` (6 sūtras)

```
1.3.4 → 1.3.5 → 1.3.6 → 1.3.7 → 1.3.8 → 1.3.9
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 100–105 |
| `pipelines/subanta_trc.py` | `__module__` | 62–67 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 27 — `3a8f7ed1427d` (6 sūtras)

```
4.1.2 → 1.3.2 → 1.3.3 → 1.3.4 → 1.3.5 → 1.3.6
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 97–102 |
| `pipelines/subanta_trc.py` | `__module__` | 58–64 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 28 — `4dab1382766c` (6 sūtras)

```
1.3.2 → 1.3.3 → 1.3.4 → 1.3.5 → 1.3.6 → 1.3.7
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 98–103 |
| `pipelines/subanta_trc.py` | `__module__` | 60–65 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 29 — `5281fb71cabc` (6 sūtras)

```
1.3.5 → 1.3.6 → 1.3.7 → 1.3.8 → 1.3.9 → 1.3.10
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 101–106 |
| `pipelines/subanta_trc.py` | `__module__` | 63–68 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 30 — `5bb9ac3f9f3e` (6 sūtras)

```
1.3.3 → 1.3.4 → 1.3.5 → 1.3.6 → 1.3.7 → 1.3.8
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 99–104 |
| `pipelines/subanta_trc.py` | `__module__` | 61–66 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 31 — `20f2a596dc9d` (5 sūtras)

```
1.1.7 → 1.1.8 → 1.1.9 → 1.1.10 → 1.1.11
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 280–286 |
| `pipelines/krdanta.py` | `__module__` | 151–156 |
| `pipelines/krdanta.py` | `__module__` | 226–231 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 32 — `317d7cb6e5dd` (5 sūtras)

```
1.1.11 → 1.1.12 → 1.1.13 → 1.1.14 → 1.1.100
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 286–291 |
| `pipelines/krdanta.py` | `__module__` | 156–160 |
| `pipelines/krdanta.py` | `__module__` | 231–235 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 33 — `3dfbc6e09b34` (5 sūtras)

```
1.1.9 → 1.1.10 → 1.1.11 → 1.1.12 → 1.1.13
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 284–288 |
| `pipelines/krdanta.py` | `__module__` | 154–158 |
| `pipelines/krdanta.py` | `__module__` | 229–233 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 34 — `4101c158c844` (5 sūtras)

```
1.1.10 → 1.1.11 → 1.1.12 → 1.1.13 → 1.1.14
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 285–289 |
| `pipelines/krdanta.py` | `__module__` | 155–159 |
| `pipelines/krdanta.py` | `__module__` | 230–234 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 35 — `a8e63ddcbf0b` (5 sūtras)

```
1.1.3 → 1.1.7 → 1.1.8 → 1.1.9 → 1.1.10
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 279–285 |
| `pipelines/krdanta.py` | `__module__` | 150–155 |
| `pipelines/krdanta.py` | `__module__` | 225–230 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 36 — `e6d7421d5509` (5 sūtras)

```
1.1.8 → 1.1.9 → 1.1.10 → 1.1.11 → 1.1.12
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 283–287 |
| `pipelines/krdanta.py` | `__module__` | 153–157 |
| `pipelines/krdanta.py` | `__module__` | 228–232 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 37 — `6ab19c106bde` (5 sūtras)

```
1.3.2 → 1.3.3 → 1.3.4 → 1.3.5 → 1.3.6
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 98–102 |
| `pipelines/subanta_trc.py` | `__module__` | 60–64 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 38 — `840e8404f097` (5 sūtras)

```
1.3.6 → 1.3.7 → 1.3.8 → 1.3.9 → 1.3.10
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 102–106 |
| `pipelines/subanta_trc.py` | `__module__` | 64–68 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 39 — `a17ea5a1a5ef` (5 sūtras)

```
1.3.3 → 1.3.4 → 1.3.5 → 1.3.6 → 1.3.7
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 99–103 |
| `pipelines/subanta_trc.py` | `__module__` | 61–65 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 40 — `a4c7233c29a6` (5 sūtras)

```
1.3.4 → 1.3.5 → 1.3.6 → 1.3.7 → 1.3.8
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 100–104 |
| `pipelines/subanta_trc.py` | `__module__` | 62–66 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 41 — `b2f4493957c0` (5 sūtras)

```
4.1.2 → 1.3.2 → 1.3.3 → 1.3.4 → 1.3.5
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 97–101 |
| `pipelines/subanta_trc.py` | `__module__` | 58–63 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 42 — `d44031b3c5e6` (5 sūtras)

```
1.3.5 → 1.3.6 → 1.3.7 → 1.3.8 → 1.3.9
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 101–105 |
| `pipelines/subanta_trc.py` | `__module__` | 63–67 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 43 — `13632519b23a` (4 sūtras)

```
1.1.12 → 1.1.13 → 1.1.14 → 1.1.100
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 287–291 |
| `pipelines/krdanta.py` | `__module__` | 157–160 |
| `pipelines/krdanta.py` | `__module__` | 232–235 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 44 — `1c22c6e677ef` (4 sūtras)

```
1.1.7 → 1.1.8 → 1.1.9 → 1.1.10
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 280–285 |
| `pipelines/krdanta.py` | `__module__` | 151–155 |
| `pipelines/krdanta.py` | `__module__` | 226–230 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 45 — `3952e827c5a8` (4 sūtras)

```
1.1.3 → 1.1.7 → 1.1.8 → 1.1.9
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 279–284 |
| `pipelines/krdanta.py` | `__module__` | 150–154 |
| `pipelines/krdanta.py` | `__module__` | 225–229 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 46 — `5c14f50b0788` (4 sūtras)

```
1.1.10 → 1.1.11 → 1.1.12 → 1.1.13
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 285–288 |
| `pipelines/krdanta.py` | `__module__` | 155–158 |
| `pipelines/krdanta.py` | `__module__` | 230–233 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 47 — `6cf4eff4b245` (4 sūtras)

```
1.1.8 → 1.1.9 → 1.1.10 → 1.1.11
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 283–286 |
| `pipelines/krdanta.py` | `__module__` | 153–156 |
| `pipelines/krdanta.py` | `__module__` | 228–231 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 48 — `a99f75bb60e0` (4 sūtras)

```
1.1.9 → 1.1.10 → 1.1.11 → 1.1.12
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 284–287 |
| `pipelines/krdanta.py` | `__module__` | 154–157 |
| `pipelines/krdanta.py` | `__module__` | 229–232 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 49 — `b9623c86e015` (4 sūtras)

```
1.1.11 → 1.1.12 → 1.1.13 → 1.1.14
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 286–289 |
| `pipelines/krdanta.py` | `__module__` | 156–159 |
| `pipelines/krdanta.py` | `__module__` | 231–234 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 50 — `17cbb3df7db3` (4 sūtras)

```
1.3.5 → 1.3.6 → 1.3.7 → 1.3.8
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 101–104 |
| `pipelines/subanta_trc.py` | `__module__` | 63–66 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 51 — `1a7cec4f7db0` (4 sūtras)

```
1.3.4 → 1.3.5 → 1.3.6 → 1.3.7
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 100–103 |
| `pipelines/subanta_trc.py` | `__module__` | 62–65 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 52 — `1b3a772cdcb4` (4 sūtras)

```
4.1.2 → 1.3.2 → 1.3.3 → 1.3.4
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 97–100 |
| `pipelines/subanta_trc.py` | `__module__` | 58–62 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 53 — `523e5bbacecc` (4 sūtras)

```
1.3.7 → 1.3.8 → 1.3.9 → 1.3.10
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 103–106 |
| `pipelines/subanta_trc.py` | `__module__` | 65–68 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 54 — `6bdd3bc758d1` (4 sūtras)

```
3.1.1 → 3.1.2 → 3.1.3 → 4.1.76
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 135–138 |
| `pipelines/taddhita_itika_etikAyana.py` | `__module__` | 134–137 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 55 — `765097fca80f` (4 sūtras)

```
1.3.6 → 1.3.7 → 1.3.8 → 1.3.9
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 102–105 |
| `pipelines/subanta_trc.py` | `__module__` | 64–67 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 56 — `8e04479469a2` (4 sūtras)

```
1.3.2 → 1.3.3 → 1.3.4 → 1.3.5
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 98–101 |
| `pipelines/subanta_trc.py` | `__module__` | 60–63 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 57 — `a72f70c19748` (4 sūtras)

```
1.3.3 → 1.3.4 → 1.3.5 → 1.3.6
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 99–102 |
| `pipelines/subanta_trc.py` | `__module__` | 61–64 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 58 — `75e7d18bcae8` (3 sūtras)

```
3.1.1 → 3.1.2 → 3.1.3
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 135–137 |
| `pipelines/krdanta.py` | `__module__` | 179–181 |
| `pipelines/krdanta.py` | `__module__` | 250–252 |
| `pipelines/taddhita_itika_etikAyana.py` | `__module__` | 134–136 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 59 — `1b8c3e8ad6ab` (3 sūtras)

```
1.1.11 → 1.1.12 → 1.1.13
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 286–288 |
| `pipelines/krdanta.py` | `__module__` | 156–158 |
| `pipelines/krdanta.py` | `__module__` | 231–233 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 60 — `47f6bf97202c` (3 sūtras)

```
1.1.7 → 1.1.8 → 1.1.9
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 280–284 |
| `pipelines/krdanta.py` | `__module__` | 151–154 |
| `pipelines/krdanta.py` | `__module__` | 226–229 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 61 — `4fe75bb63cae` (3 sūtras)

```
1.1.12 → 1.1.13 → 1.1.14
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 287–289 |
| `pipelines/krdanta.py` | `__module__` | 157–159 |
| `pipelines/krdanta.py` | `__module__` | 232–234 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 62 — `63ae496893cf` (3 sūtras)

```
1.1.10 → 1.1.11 → 1.1.12
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 285–287 |
| `pipelines/krdanta.py` | `__module__` | 155–157 |
| `pipelines/krdanta.py` | `__module__` | 230–232 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 63 — `66245062cefc` (3 sūtras)

```
1.1.3 → 1.1.7 → 1.1.8
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 279–283 |
| `pipelines/krdanta.py` | `__module__` | 150–153 |
| `pipelines/krdanta.py` | `__module__` | 225–228 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 64 — `6914d3d7b6e6` (3 sūtras)

```
1.1.8 → 1.1.9 → 1.1.10
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 283–285 |
| `pipelines/krdanta.py` | `__module__` | 153–155 |
| `pipelines/krdanta.py` | `__module__` | 228–230 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 65 — `9903c72140f3` (3 sūtras)

```
1.1.13 → 1.1.14 → 1.1.100
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 288–291 |
| `pipelines/krdanta.py` | `__module__` | 158–160 |
| `pipelines/krdanta.py` | `__module__` | 233–235 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 66 — `c1455e490361` (3 sūtras)

```
1.1.9 → 1.1.10 → 1.1.11
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 284–286 |
| `pipelines/krdanta.py` | `__module__` | 154–156 |
| `pipelines/krdanta.py` | `__module__` | 229–231 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 67 — `21fa4e01ad26` (3 sūtras)

```
1.3.7 → 1.3.8 → 1.3.9
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 103–105 |
| `pipelines/subanta_trc.py` | `__module__` | 65–67 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 68 — `5bf4cae32a23` (3 sūtras)

```
1.3.5 → 1.3.6 → 1.3.7
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 101–103 |
| `pipelines/subanta_trc.py` | `__module__` | 63–65 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 69 — `66e2d79eaa75` (3 sūtras)

```
1.3.2 → 1.3.3 → 1.3.4
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 98–100 |
| `pipelines/subanta_trc.py` | `__module__` | 60–62 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 70 — `6756b5d8b4cd` (3 sūtras)

```
3.1.2 → 3.1.3 → 4.1.76
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 136–138 |
| `pipelines/taddhita_itika_etikAyana.py` | `__module__` | 135–137 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 71 — `7214efadb40d` (3 sūtras)

```
1.3.8 → 1.3.9 → 1.3.10
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 104–106 |
| `pipelines/subanta_trc.py` | `__module__` | 66–68 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 72 — `8c034b2a993b` (3 sūtras)

```
1.3.6 → 1.3.7 → 1.3.8
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 102–104 |
| `pipelines/subanta_trc.py` | `__module__` | 64–66 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 73 — `9a26ceb9de86` (3 sūtras)

```
4.1.2 → 1.3.2 → 1.3.3
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 97–99 |
| `pipelines/subanta_trc.py` | `__module__` | 58–61 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 74 — `c8dc868ade2e` (3 sūtras)

```
1.3.3 → 1.3.4 → 1.3.5
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 99–101 |
| `pipelines/subanta_trc.py` | `__module__` | 61–63 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 75 — `ffd861237d84` (3 sūtras)

```
1.3.4 → 1.3.5 → 1.3.6
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 100–102 |
| `pipelines/subanta_trc.py` | `__module__` | 62–64 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.
