while true; do
  read -p "Enter start of profile folder name: " prefix
  shopt -s nullglob nocaseglob
  matches=(~/.local/share/ice/firefox/"$prefix"*/)
  shopt -u nullglob nocaseglob
  if [ "${#matches[@]}" -ne 1 ]; then
    echo "found ${#matches[@]} matching folders, try again"
    continue
  fi
  target="${matches[0]}chrome/userChrome.css"
  mkdir -p "${matches[0]}chrome"
  if [ -s "$target" ] && [ "$(tail -c1 "$target")" != "" ]; then
    echo >> "$target"
  fi
  cat >> "$target" <<'EOF'
navigator-toolbox { border-bottom: none !important; }
nav-bar,
identity-box,
tabbrowser-tabs,
TabsToolbar,
nav-bar * { visibility: collapse !important; }
#TabsToolbar {
  display: none !important;
}
EOF
  echo "appended css to $target"
done

