def analyze_log(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    suspicious = [line for line in lines if "failed" in line.lower() or "error" in line.lower()]

    print(f"Ukupan broj linija: {len(lines)}")
    print(f"Sumnjive linije: {len(suspicious)}")
    for line in suspicious:
        print("[!] " + line.strip())

if __name__ == "__main__":
    path = input("Unesi putanju do log fajla: ").strip()
    analyze_log(path)
