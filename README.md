
## 🔹 **Commit & cambios**

* **Hacer un commit nuevo**

  ```bash
  git add .
  git commit -m "mensaje"
  ```

* **Modificar el último commit (mensaje y/o archivos)**

  ```bash
  git commit --amend
  ```

* **Borrar el último commit pero mantener los cambios en el working directory**

  ```bash
  git reset --soft HEAD~1
  ```

* **Borrar el último commit y los cambios también**

  ```bash
  git reset --hard HEAD~1
  ```

---

## 🔹 **Branches**

* **Crear un branch nuevo**

  ```bash
  git checkout -b nombre_branch
  ```

* **Cambiar de branch**

  ```bash
  git checkout nombre_branch
  ```

* **Borrar un branch local**

  ```bash
  git branch -d nombre_branch
  ```

  (si no se deja borrar porque no está mergeado, usar `-D` en lugar de `-d`)

* **Borrar un branch remoto**

  ```bash
  git push origin --delete nombre_branch
  ```

---

## 🔹 **Merge & sincronización**

* **Hacer merge de otra branch a la actual**

  ```bash
  git merge nombre_branch
  ```

* **Subir cambios al remoto**

  ```bash
  git push origin nombre_branch
  ```

* **Traer cambios del remoto y mezclarlos**

  ```bash
  git pull origin main
  ```

* **Forzar que el remoto sobrescriba lo local**

  ```bash
  git fetch origin
  git reset --hard origin/main
  ```

* **Forzar que lo local sobrescriba lo remoto**

  ```bash
  git push origin main --force
  ```

---

## 🔹 **Estado & utilidad**

* **Ver el estado de los archivos**

  ```bash
  git status
  ```

* **Ver historial de commits**

  ```bash
  git log --oneline --graph --decorate --all
  ```

* **Ver a qué remoto apunta tu repo**

  ```bash
  git remote -v
  ```

---

