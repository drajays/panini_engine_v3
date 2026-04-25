# Scheduling block audit (``apply_rule`` chains)

Read-only AST scan of **ordered** ``apply_rule("x.y.z", …)`` calls.  Strings that are not the first argument to ``apply_rule`` are ignored.

- **scanned_py_files**: `20`
- **duplicate_cross_file_groups**: `39`

## Duplicate groups (longest first)

### 1 — `d77483ce8421` (10 sūtras)

```
4.1.2 → 1.3.2 → 1.3.3 → 1.3.4 → 1.3.5 → 1.3.6 → 1.3.7 → 1.3.8 → 1.3.9 → 1.3.10
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 97–106 |
| `pipelines/subanta_trc.py` | `__module__` | 58–68 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 2 — `377883e69df5` (9 sūtras)

```
4.1.2 → 1.3.2 → 1.3.3 → 1.3.4 → 1.3.5 → 1.3.6 → 1.3.7 → 1.3.8 → 1.3.9
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 97–105 |
| `pipelines/subanta_trc.py` | `__module__` | 58–67 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 3 — `d448e8fccbea` (9 sūtras)

```
1.3.2 → 1.3.3 → 1.3.4 → 1.3.5 → 1.3.6 → 1.3.7 → 1.3.8 → 1.3.9 → 1.3.10
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 98–106 |
| `pipelines/subanta_trc.py` | `__module__` | 60–68 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 4 — `1ebe1e3f845d` (8 sūtras)

```
4.1.2 → 1.3.2 → 1.3.3 → 1.3.4 → 1.3.5 → 1.3.6 → 1.3.7 → 1.3.8
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 97–104 |
| `pipelines/subanta_trc.py` | `__module__` | 58–66 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 5 — `2684f2bc3891` (8 sūtras)

```
1.3.3 → 1.3.4 → 1.3.5 → 1.3.6 → 1.3.7 → 1.3.8 → 1.3.9 → 1.3.10
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 99–106 |
| `pipelines/subanta_trc.py` | `__module__` | 61–68 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 6 — `c4820671bdd5` (8 sūtras)

```
1.3.2 → 1.3.3 → 1.3.4 → 1.3.5 → 1.3.6 → 1.3.7 → 1.3.8 → 1.3.9
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 98–105 |
| `pipelines/subanta_trc.py` | `__module__` | 60–67 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 7 — `049307f22e75` (7 sūtras)

```
1.3.2 → 1.3.3 → 1.3.4 → 1.3.5 → 1.3.6 → 1.3.7 → 1.3.8
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 98–104 |
| `pipelines/subanta_trc.py` | `__module__` | 60–66 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 8 — `3e4f30abd4f9` (7 sūtras)

```
4.1.2 → 1.3.2 → 1.3.3 → 1.3.4 → 1.3.5 → 1.3.6 → 1.3.7
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 97–103 |
| `pipelines/subanta_trc.py` | `__module__` | 58–65 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 9 — `90a7fb70876e` (7 sūtras)

```
1.3.3 → 1.3.4 → 1.3.5 → 1.3.6 → 1.3.7 → 1.3.8 → 1.3.9
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 99–105 |
| `pipelines/subanta_trc.py` | `__module__` | 61–67 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 10 — `98981d7d2b98` (7 sūtras)

```
1.3.4 → 1.3.5 → 1.3.6 → 1.3.7 → 1.3.8 → 1.3.9 → 1.3.10
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 100–106 |
| `pipelines/subanta_trc.py` | `__module__` | 62–68 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 11 — `298fec72950a` (6 sūtras)

```
1.3.4 → 1.3.5 → 1.3.6 → 1.3.7 → 1.3.8 → 1.3.9
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 100–105 |
| `pipelines/subanta_trc.py` | `__module__` | 62–67 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 12 — `3a8f7ed1427d` (6 sūtras)

```
4.1.2 → 1.3.2 → 1.3.3 → 1.3.4 → 1.3.5 → 1.3.6
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 97–102 |
| `pipelines/subanta_trc.py` | `__module__` | 58–64 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 13 — `4dab1382766c` (6 sūtras)

```
1.3.2 → 1.3.3 → 1.3.4 → 1.3.5 → 1.3.6 → 1.3.7
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 98–103 |
| `pipelines/subanta_trc.py` | `__module__` | 60–65 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 14 — `5281fb71cabc` (6 sūtras)

```
1.3.5 → 1.3.6 → 1.3.7 → 1.3.8 → 1.3.9 → 1.3.10
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 101–106 |
| `pipelines/subanta_trc.py` | `__module__` | 63–68 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 15 — `5bb9ac3f9f3e` (6 sūtras)

```
1.3.3 → 1.3.4 → 1.3.5 → 1.3.6 → 1.3.7 → 1.3.8
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 99–104 |
| `pipelines/subanta_trc.py` | `__module__` | 61–66 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 16 — `6ab19c106bde` (5 sūtras)

```
1.3.2 → 1.3.3 → 1.3.4 → 1.3.5 → 1.3.6
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 98–102 |
| `pipelines/subanta_trc.py` | `__module__` | 60–64 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 17 — `840e8404f097` (5 sūtras)

```
1.3.6 → 1.3.7 → 1.3.8 → 1.3.9 → 1.3.10
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 102–106 |
| `pipelines/subanta_trc.py` | `__module__` | 64–68 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 18 — `a17ea5a1a5ef` (5 sūtras)

```
1.3.3 → 1.3.4 → 1.3.5 → 1.3.6 → 1.3.7
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 99–103 |
| `pipelines/subanta_trc.py` | `__module__` | 61–65 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 19 — `a4c7233c29a6` (5 sūtras)

```
1.3.4 → 1.3.5 → 1.3.6 → 1.3.7 → 1.3.8
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 100–104 |
| `pipelines/subanta_trc.py` | `__module__` | 62–66 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 20 — `b2f4493957c0` (5 sūtras)

```
4.1.2 → 1.3.2 → 1.3.3 → 1.3.4 → 1.3.5
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 97–101 |
| `pipelines/subanta_trc.py` | `__module__` | 58–63 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 21 — `d44031b3c5e6` (5 sūtras)

```
1.3.5 → 1.3.6 → 1.3.7 → 1.3.8 → 1.3.9
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 101–105 |
| `pipelines/subanta_trc.py` | `__module__` | 63–67 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 22 — `17cbb3df7db3` (4 sūtras)

```
1.3.5 → 1.3.6 → 1.3.7 → 1.3.8
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 101–104 |
| `pipelines/subanta_trc.py` | `__module__` | 63–66 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 23 — `1a7cec4f7db0` (4 sūtras)

```
1.3.4 → 1.3.5 → 1.3.6 → 1.3.7
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 100–103 |
| `pipelines/subanta_trc.py` | `__module__` | 62–65 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 24 — `1b3a772cdcb4` (4 sūtras)

```
4.1.2 → 1.3.2 → 1.3.3 → 1.3.4
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 97–100 |
| `pipelines/subanta_trc.py` | `__module__` | 58–62 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 25 — `523e5bbacecc` (4 sūtras)

```
1.3.7 → 1.3.8 → 1.3.9 → 1.3.10
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 103–106 |
| `pipelines/subanta_trc.py` | `__module__` | 65–68 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 26 — `6bdd3bc758d1` (4 sūtras)

```
3.1.1 → 3.1.2 → 3.1.3 → 4.1.76
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 135–138 |
| `pipelines/taddhita_itika_etikAyana.py` | `__module__` | 134–137 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 27 — `765097fca80f` (4 sūtras)

```
1.3.6 → 1.3.7 → 1.3.8 → 1.3.9
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 102–105 |
| `pipelines/subanta_trc.py` | `__module__` | 64–67 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 28 — `8e04479469a2` (4 sūtras)

```
1.3.2 → 1.3.3 → 1.3.4 → 1.3.5
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 98–101 |
| `pipelines/subanta_trc.py` | `__module__` | 60–63 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 29 — `a72f70c19748` (4 sūtras)

```
1.3.3 → 1.3.4 → 1.3.5 → 1.3.6
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 99–102 |
| `pipelines/subanta_trc.py` | `__module__` | 61–64 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 30 — `75e7d18bcae8` (3 sūtras)

```
3.1.1 → 3.1.2 → 3.1.3
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 135–137 |
| `pipelines/krdanta.py` | `__module__` | 169–171 |
| `pipelines/krdanta.py` | `__module__` | 230–232 |
| `pipelines/taddhita_itika_etikAyana.py` | `__module__` | 134–136 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 31 — `21fa4e01ad26` (3 sūtras)

```
1.3.7 → 1.3.8 → 1.3.9
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 103–105 |
| `pipelines/subanta_trc.py` | `__module__` | 65–67 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 32 — `5bf4cae32a23` (3 sūtras)

```
1.3.5 → 1.3.6 → 1.3.7
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 101–103 |
| `pipelines/subanta_trc.py` | `__module__` | 63–65 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 33 — `66e2d79eaa75` (3 sūtras)

```
1.3.2 → 1.3.3 → 1.3.4
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 98–100 |
| `pipelines/subanta_trc.py` | `__module__` | 60–62 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 34 — `6756b5d8b4cd` (3 sūtras)

```
3.1.2 → 3.1.3 → 4.1.76
```

| File | Scope | Lines |
|---|---|---|
| `core/canonical_pipelines.py` | `__module__` | 136–138 |
| `pipelines/taddhita_itika_etikAyana.py` | `__module__` | 135–137 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 35 — `7214efadb40d` (3 sūtras)

```
1.3.8 → 1.3.9 → 1.3.10
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 104–106 |
| `pipelines/subanta_trc.py` | `__module__` | 66–68 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 36 — `8c034b2a993b` (3 sūtras)

```
1.3.6 → 1.3.7 → 1.3.8
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 102–104 |
| `pipelines/subanta_trc.py` | `__module__` | 64–66 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 37 — `9a26ceb9de86` (3 sūtras)

```
4.1.2 → 1.3.2 → 1.3.3
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 97–99 |
| `pipelines/subanta_trc.py` | `__module__` | 58–61 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 38 — `c8dc868ade2e` (3 sūtras)

```
1.3.3 → 1.3.4 → 1.3.5
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 99–101 |
| `pipelines/subanta_trc.py` | `__module__` | 61–63 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.

### 39 — `ffd861237d84` (3 sūtras)

```
1.3.4 → 1.3.5 → 1.3.6
```

| File | Scope | Lines |
|---|---|---|
| `pipelines/devendra.py` | `__module__` | 100–102 |
| `pipelines/subanta_trc.py` | `__module__` | 62–64 |

**Note:** identical windows often mean “extract to ``core.canonical_pipelines`` and call one helper”, not that the sūtras are duplicated in ``sutras/``.
