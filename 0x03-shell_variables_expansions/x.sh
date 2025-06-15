#!/bin/bash

# 100-decimal_to_hexadecimal
cat << 'EOF' > 100-decimal_to_hexadecimal
#!/bin/bash
printf "%x\n" "$DECIMAL"
EOF
chmod +x 100-decimal_to_hexadecimal

# 101-rot13
cat << 'EOF' > 101-rot13
#!/bin/bash
tr 'A-Za-z' 'N-ZA-Mn-za-m'
EOF
chmod +x 101-rot13

# 102-odd
cat << 'EOF' > 102-odd
#!/bin/bash
awk 'NR % 2 == 1'
EOF
chmod +x 102-odd

# 103-water_and_stir
cat << 'EOF' > 103-water_and_stir
#!/bin/bash
echo "$(( $(echo "$WATER" | tr 'water' '01234') + $(echo "$STIR" | tr 'stir.' '01234') ))" | tr '0123456789' 'bestchol'
EOF
chmod +x 103-water_and_stir

echo "✅ Advanced task scripts created successfully."
