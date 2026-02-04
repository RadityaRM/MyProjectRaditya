<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for, jsonify, send_file, Response
import mysql.connector
import decimal
from io import BytesIO, StringIO
from xhtml2pdf import pisa
import datetime
import re
import csv
=======
from flask import Flask, render_template, request, redirect, url_for, jsonify, send_file
import mysql.connector
import decimal
from io import BytesIO
from xhtml2pdf import pisa
import datetime
import re
>>>>>>> 4e5da73ad724034d2f81f139bbd87aead75aae72

app = Flask(__name__)

Raditya_db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '',
    'database': 'raport_raditya'
}

def get_db_connection():
    return mysql.connector.connect(**Raditya_db_config)

def normalize(Raditya_rows):
    if Raditya_rows is None:
        return Raditya_rows
    if isinstance(Raditya_rows, dict):
        Raditya_rows = [Raditya_rows]
    try:
        for Raditya_r in Raditya_rows:
            if not isinstance(Raditya_r, dict):
                continue
            for Raditya_k, Raditya_v in list(Raditya_r.items()):
                if isinstance(Raditya_v, decimal.Decimal):
                    if Raditya_v == Raditya_v.to_integral_value():
                        Raditya_r[Raditya_k] = int(Raditya_v)
                    else:
                        Raditya_r[Raditya_k] = float(Raditya_v)
    except Exception:
        pass
    return Raditya_rows

def get_enum_options_from_column(table, column):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute(f"SHOW COLUMNS FROM `{table}` LIKE %s", (column,))
        Raditya_row = cur.fetchone()
        if not Raditya_row:
            return []
        Raditya_col_type = Raditya_row[1]
        Raditya_m = re.match(r"^enum\((.*)\)$", Raditya_col_type, re.IGNORECASE)
        if not Raditya_m:
            return []
        Raditya_inner = Raditya_m.group(1)
        Raditya_parts = []
        for Raditya_p in Raditya_inner.split(","):
            Raditya_p = Raditya_p.strip()
            if Raditya_p.startswith("'") and Raditya_p.endswith("'"):
                Raditya_parts.append(Raditya_p[1:-1])
            else:
                Raditya_parts.append(Raditya_p.strip("'\""))
        return Raditya_parts
    finally:
        conn.close()

@app.route('/')
def index():
<<<<<<< HEAD
    f_semester = request.args.get('semester') or None
    f_tahun = request.args.get('tahun') or request.args.get('tahun_ajaran') or None
    f_id_kelas = request.args.get('id_kelas') or None

    conn = get_db_connection()
    try:
        cur = conn.cursor(dictionary=True)

        query_students = """
=======
    conn = get_db_connection()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("""
>>>>>>> 4e5da73ad724034d2f81f139bbd87aead75aae72
            SELECT s.NIS_Raditya, s.Nama_Raditya,
                   ROUND(IFNULL(AVG(n.Nilai_Akhir_Raditya),0),2) AS Avg_Final
            FROM raditya_siswa s
            LEFT JOIN raditya_nilai n ON s.NIS_Raditya = n.NIS_Raditya
<<<<<<< HEAD
        """
        params = []
        where_clauses = []
        if f_semester:
            where_clauses.append("n.Semester_Raditya = %s")
            params.append(f_semester)
        if f_tahun:
            where_clauses.append("n.Tahun_Ajaran_Raditya = %s")
            params.append(f_tahun)
        if f_id_kelas:
            where_clauses.append("s.ID_Kelas = %s")
            params.append(f_id_kelas)

        if where_clauses:
            query_students += " WHERE " + " AND ".join(where_clauses)

        query_students += " GROUP BY s.NIS_Raditya ORDER BY s.NIS_Raditya ASC"
        cur.execute(query_students, params)
=======
            GROUP BY s.NIS_Raditya
            ORDER BY s.NIS_Raditya ASC
        """)
>>>>>>> 4e5da73ad724034d2f81f139bbd87aead75aae72
        Raditya_students = cur.fetchall()

        cur.execute("""
            SELECT m.ID_Mapel_Raditya, m.Nama_Mapel_Raditya,
                   COUNT(n.ID_Nilai_Raditya) AS count_scores,
                   ROUND(IFNULL(AVG(n.Nilai_Akhir_Raditya),0),2) AS avg_score
            FROM raditya_mapel m
            LEFT JOIN raditya_nilai n ON m.ID_Mapel_Raditya = n.ID_Mapel_Raditya
            GROUP BY m.ID_Mapel_Raditya
            ORDER BY m.Nama_Mapel_Raditya
        """)
<<<<<<< HEAD
        try:
            Raditya_mapel_stats = cur.fetchall()
        except Exception:
            cur.execute("""
                SELECT m.ID_Mapel_Raditya, m.Nama_Mapel_Raditya,
                       COUNT(n.ID_Nilai_Raditya) AS count_scores,
                       ROUND(IFNULL(AVG(n.Nilai_Akhir_Raditya),0),2) AS avg_score
                FROM raditya_mapel m
                LEFT JOIN raditya_nilai n ON m.ID_Mapel_Raditya = n.ID_Mapel_Radel
                GROUP BY m.ID_Mapel_Raditya
                ORDER BY m.Nama_Mapel_Raditya
            """)
            try:
                Raditya_mapel_stats = cur.fetchall()
            except Exception:
                cur.execute("SELECT ID_Mapel_Raditya, Nama_Mapel_Raditya FROM raditya_mapel ORDER BY Nama_Mapel_Raditya")
                Raditya_mapel_stats = cur.fetchall()
=======
        Raditya_mapel_stats = cur.fetchall()
>>>>>>> 4e5da73ad724034d2f81f139bbd87aead75aae72

        cur.execute("SELECT NIS_Raditya, Nama_Raditya FROM raditya_siswa ORDER BY NIS_Raditya ASC")
        Raditya_siswa_list = cur.fetchall()

        cur.execute("SELECT ID_Mapel_Raditya, Nama_Mapel_Raditya FROM raditya_mapel ORDER BY Nama_Mapel_Raditya")
        Raditya_mapel_list = cur.fetchall()

        cur.execute("SELECT ID_Kelas_Raditya, Jurusan_Raditya, Tingkat_Raditya FROM raditya_kelas ORDER BY Tingkat_Raditya, Jurusan_Raditya")
        Raditya_kelas_list = cur.fetchall()
<<<<<<< HEAD

        cur.execute("SELECT DISTINCT Semester_Raditya AS sem FROM raditya_nilai ORDER BY Semester_Raditya ASC")
        Raditya_semester_list = [r['sem'] for r in cur.fetchall() if r and r.get('sem') is not None]

        cur.execute("SELECT DISTINCT Tahun_Ajaran_Raditya AS th FROM raditya_nilai ORDER BY Tahun_Ajaran_Raditya DESC")
        Raditya_tahun_list = [r['th'] for r in cur.fetchall() if r and r.get('th') is not None]

=======
>>>>>>> 4e5da73ad724034d2f81f139bbd87aead75aae72
    finally:
        conn.close()

    jk_options = get_enum_options_from_column('raditya_siswa', 'Jenis_Kelamin_Raditya')

    normalize(Raditya_students)
    normalize(Raditya_mapel_stats)
    return render_template('Home.html',
                           students=Raditya_students,
                           mapel_stats=Raditya_mapel_stats,
                           siswa=Raditya_siswa_list,
                           mapel=Raditya_mapel_list,
                           kelas=Raditya_kelas_list,
<<<<<<< HEAD
                           jk_options=jk_options,
                           semester_list=Raditya_semester_list,
                           tahun_list=Raditya_tahun_list,
                           active_filters={'semester': f_semester, 'tahun': f_tahun, 'id_kelas': f_id_kelas})
=======
                           jk_options=jk_options)
>>>>>>> 4e5da73ad724034d2f81f139bbd87aead75aae72

@app.route('/mapel/<int:Raditya_id>/data')
def mapel_data(Raditya_id):
    conn = get_db_connection()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("""
            SELECT n.ID_Nilai_Raditya, n.NIS_Raditya, s.Nama_Raditya, n.Nilai_Tugas_Raditya,
                   n.Nilai_UTS_Raditya, n.Nilai_UAS_Raditya, n.Nilai_Akhir_Raditya
            FROM raditya_nilai n
            LEFT JOIN raditya_siswa s ON n.NIS_Raditya = s.NIS_Raditya
            WHERE n.ID_Mapel_Raditya = %s
            ORDER BY n.NIS_Raditya ASC
        """, (Raditya_id,))
        Raditya_rows = cur.fetchall()
    finally:
        conn.close()
    normalize(Raditya_rows)
    return jsonify(Raditya_rows or [])

@app.route('/student/<int:Raditya_nis>/nilai')
def student_nilai(Raditya_nis):
    conn = get_db_connection()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("""
            SELECT n.ID_Nilai_Raditya, m.Nama_Mapel_Raditya, n.Nilai_Tugas_Raditya,
                   n.Nilai_UTS_Raditya, n.Nilai_UAS_Raditya, n.Nilai_Akhir_Raditya
            FROM raditya_nilai n
            LEFT JOIN raditya_mapel m ON n.ID_Mapel_Raditya = m.ID_Mapel_Raditya
            WHERE n.NIS_Raditya = %s
            ORDER BY m.Nama_Mapel_Raditya
        """, (Raditya_nis,))
        Raditya_rows = cur.fetchall()
    finally:
        conn.close()
    normalize(Raditya_rows)
    return jsonify(Raditya_rows or [])

@app.route('/siswa/<int:nis>/json')
def siswa_detail_json(nis):
    conn = get_db_connection()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM raditya_siswa WHERE NIS_Raditya = %s", (nis,))
        row = cur.fetchone()
    finally:
        conn.close()

    if row:
        try:
            t = row.get('Tanggal_Lahir_Raditya')
            if t is None:
                row['Tanggal_Lahir_Raditya'] = ''
            else:
                if isinstance(t, (datetime.date, datetime.datetime)):
                    row['Tanggal_Lahir_Raditya'] = t.strftime('%Y-%m-%d')
                else:
                    m = re.search(r'(\d{4}-\d{2}-\d{2})', str(t))
                    row['Tanggal_Lahir_Raditya'] = m.group(1) if m else ''
        except Exception:
            row['Tanggal_Lahir_Raditya'] = ''

    normalize(row)
    return jsonify(row or {})

@app.route('/nilai/<int:id>/json')
def nilai_json(id):
    conn = get_db_connection()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM raditya_nilai WHERE ID_Nilai_Raditya = %s", (id,))
        row = cur.fetchone()
    finally:
        conn.close()
    normalize(row)
    return jsonify(row or {})

@app.route('/nilai/add', methods=['POST'])
def nilai_add():
    Raditya_nis = request.form.get('nis')
    Raditya_id_mapel = request.form.get('id_mapel')
    try:
        Raditya_tugas = float(request.form.get('nilai_tugas', 0))
    except Exception:
        Raditya_tugas = 0.0
    try:
        Raditya_uts = float(request.form.get('nilai_uts', 0))
    except Exception:
        Raditya_uts = 0.0
    try:
        Raditya_uas = float(request.form.get('nilai_uas', 0))
    except Exception:
        Raditya_uas = 0.0

    Raditya_nilai_akhir = int(round(Raditya_tugas * 0.3 + Raditya_uts * 0.3 + Raditya_uas * 0.4))
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        try:
            Raditya_nis_db = int(Raditya_nis) if Raditya_nis is not None and Raditya_nis != '' else None
        except Exception:
            Raditya_nis_db = Raditya_nis
        cur.execute("""INSERT INTO raditya_nilai
                       (NIS_Raditya, ID_Mapel_Raditya, Nilai_Tugas_Raditya, Nilai_UTS_Raditya, Nilai_UAS_Raditya, Nilai_Akhir_Raditya, Semester_Raditya, Tahun_Ajaran_Raditya)
                       VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",
                    (Raditya_nis_db, Raditya_id_mapel, int(round(Raditya_tugas)), int(round(Raditya_uts)), int(round(Raditya_uas)), Raditya_nilai_akhir,
                     request.form.get('semester', 1), request.form.get('tahun_ajaran', datetime.datetime.now().year)))
        conn.commit()
    finally:
        conn.close()
    return redirect(url_for('index', status='created'))

@app.route('/nilai/edit/<int:Raditya_id>', methods=['POST'])
def nilai_edit(Raditya_id):
    Raditya_nis = request.form.get('nis')
    Raditya_id_mapel = request.form.get('id_mapel')
    try:
        Raditya_tugas = float(request.form.get('nilai_tugas', 0))
    except Exception:
        Raditya_tugas = 0.0
    try:
        Raditya_uts = float(request.form.get('nilai_uts', 0))
    except Exception:
        Raditya_uts = 0.0
    try:
        Raditya_uas = float(request.form.get('nilai_uas', 0))
    except Exception:
        Raditya_uas = 0.0

    Raditya_nilai_akhir = int(round(Raditya_tugas * 0.3 + Raditya_uts * 0.3 + Raditya_uas * 0.4))
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        try:
            Raditya_nis_db = int(Raditya_nis) if Raditya_nis is not None and Raditya_nis != '' else None
        except Exception:
            Raditya_nis_db = Raditya_nis
        cur.execute("""UPDATE raditya_nilai SET NIS_Raditya=%s, ID_Mapel_Raditya=%s,
                       Nilai_Tugas_Raditya=%s, Nilai_UTS_Raditya=%s, Nilai_UAS_Raditya=%s,
                       Nilai_Akhir_Raditya=%s, Semester_Raditya=%s, Tahun_Ajaran_Raditya=%s
                       WHERE ID_Nilai_Raditya=%s""",
                    (Raditya_nis_db, Raditya_id_mapel, int(round(Raditya_tugas)), int(round(Raditya_uts)), int(round(Raditya_uas)), Raditya_nilai_akhir,
                     request.form.get('semester', 1), request.form.get('tahun_ajaran', datetime.datetime.now().year), Raditya_id))
        conn.commit()
    finally:
        conn.close()
    return redirect(url_for('index', status='updated'))

@app.route('/nilai/delete/<int:Raditya_id>')
def nilai_delete(Raditya_id):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM raditya_nilai WHERE ID_Nilai_Raditya=%s", (Raditya_id,))
        conn.commit()
    finally:
        conn.close()
    return redirect(url_for('index', status='deleted'))

@app.route('/siswa/next-nis')
def next_nis():
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT MAX(NIS_Raditya) FROM raditya_siswa")
        Raditya_last = cur.fetchone()
        Raditya_last_val = Raditya_last[0] if Raditya_last else None
        try:
            Raditya_next_nis_val = int(Raditya_last_val) + 1 if Raditya_last_val is not None else 10243309
        except Exception:
            Raditya_next_nis_val = 10243309
    finally:
        conn.close()
    return jsonify({"next_nis": Raditya_next_nis_val})

@app.route('/siswa/add', methods=['POST'])
def siswa_add():
    Raditya_nis = request.form.get('nis')
    Raditya_nama = request.form.get('nama')
    Raditya_jenis_kelamin = request.form.get('jenis_kelamin') or request.form.get('Jenis_Kelamin_Raditya') or ''
    Raditya_tempat = request.form.get('tempat_lahir') or ''
    Raditya_tanggal = request.form.get('tanggal_lahir') or '2000-01-01'
    Raditya_alamat = request.form.get('alamat') or ''
    Raditya_id_kelas = request.form.get('id_kelas') or request.form.get('kelas') or 1

    conn = get_db_connection()
    try:
        cur = conn.cursor()
        if not Raditya_nis or Raditya_nis == '':
            cur.execute("SELECT MAX(NIS_Raditya) FROM raditya_siswa")
            Raditya_last = cur.fetchone()
            Raditya_last_val = Raditya_last[0] if Raditya_last else None
            try:
                Raditya_nis_db = int(Raditya_last_val) + 1 if Raditya_last_val is not None else 10243309
            except Exception:
                Raditya_nis_db = 10243309
        else:
            try:
                Raditya_nis_db = int(Raditya_nis)
            except Exception:
                Raditya_nis_db = Raditya_nis

        cur.execute("""INSERT INTO raditya_siswa
                       (NIS_Raditya, Nama_Raditya, Jenis_Kelamin_Raditya, Tempat_Lahir_Raditya, Tanggal_Lahir_Raditya, Alamat_Raditya, ID_Kelas)
                       VALUES (%s,%s,%s,%s,%s,%s,%s)""",
                    (Raditya_nis_db, Raditya_nama, Raditya_jenis_kelamin, Raditya_tempat, Raditya_tanggal, Raditya_alamat, Raditya_id_kelas))
        conn.commit()
    finally:
        conn.close()
    return redirect(url_for('index', status='siswa_created'))

@app.route('/siswa/edit/<int:Raditya_orig_nis>', methods=['POST'])
def siswa_edit(Raditya_orig_nis):
    Raditya_new_nis = request.form.get('nis')
    Raditya_nama = request.form.get('nama')
    Raditya_jenis_kelamin = request.form.get('jenis_kelamin') or ''
    Raditya_tempat = request.form.get('tempat_lahir') or ''
    Raditya_tanggal = request.form.get('tanggal_lahir') or '2000-01-01'
    Raditya_alamat = request.form.get('alamat') or ''
    Raditya_id_kelas = request.form.get('id_kelas') or 1

    try:
        Raditya_new_nis_db = int(Raditya_new_nis) if Raditya_new_nis is not None and Raditya_new_nis != '' else Raditya_orig_nis
    except Exception:
        Raditya_new_nis_db = Raditya_new_nis or Raditya_orig_nis

    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("""UPDATE raditya_siswa SET
                       NIS_Raditya=%s, Nama_Raditya=%s, Jenis_Kelamin_Raditya=%s, Tempat_Lahir_Raditya=%s,
                       Tanggal_Lahir_Raditya=%s, Alamat_Raditya=%s, ID_Kelas=%s
                       WHERE NIS_Raditya=%s""",
                    (Raditya_new_nis_db, Raditya_nama, Raditya_jenis_kelamin, Raditya_tempat, Raditya_tanggal, Raditya_alamat, Raditya_id_kelas, Raditya_orig_nis))
        conn.commit()
    finally:
        conn.close()
    return redirect(url_for('index', status='siswa_updated'))

@app.route('/siswa/list')
def siswa_list():
    conn = get_db_connection()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT NIS_Raditya, Nama_Raditya FROM raditya_siswa ORDER BY NIS_Raditya ASC")
        Raditya_rows = cur.fetchall()
    finally:
        conn.close()
    return jsonify(Raditya_rows or [])

<<<<<<< HEAD
@app.route('/cetak-raport-all')
def cetak_raport_all():
    f_semester = request.args.get('semester') or None
    f_tahun = request.args.get('tahun') or request.args.get('tahun_ajaran') or None
    f_id_kelas = request.args.get('id_kelas') or None

    conn = get_db_connection()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT ID_Mapel_Raditya, Nama_Mapel_Raditya FROM raditya_mapel ORDER BY Nama_Mapel_Raditya")
        mapels = cur.fetchall() or []
        mapel_ids = [m['ID_Mapel_Raditya'] for m in mapels]
        mapel_names = [m['Nama_Mapel_Raditya'] for m in mapels]

        params_students = []
        sql_students = """
            SELECT s.NIS_Raditya, s.Nama_Raditya,
                   IFNULL(k.Tingkat_Raditya,'') AS Tingkat_Raditya, IFNULL(k.Jurusan_Raditya,'') AS Jurusan_Raditya
            FROM raditya_siswa s
            LEFT JOIN raditya_kelas k ON s.ID_Kelas = k.ID_Kelas_Raditya
        """
        if f_id_kelas:
            sql_students += " WHERE s.ID_Kelas = %s"
            params_students.append(f_id_kelas)
        sql_students += " ORDER BY s.Nama_Raditya"
        cur.execute(sql_students, params_students)
        students = cur.fetchall() or []

        rows = []
        for s in students:
            nis = s['NIS_Raditya']
            params = [nis]
            sql_nilai = """
                SELECT n.ID_Mapel_Raditya, n.Nilai_Akhir_Raditya
                FROM raditya_nilai n
                WHERE n.NIS_Raditya = %s
            """
            if f_semester:
                sql_nilai += " AND n.Semester_Raditya = %s"
                params.append(f_semester)
            if f_tahun:
                sql_nilai += " AND n.Tahun_Ajaran_Raditya = %s"
                params.append(f_tahun)
            cur.execute(sql_nilai, params)
            nilai_list = cur.fetchall() or []

            nilai_map = {n['ID_Mapel_Raditya']: n['Nilai_Akhir_Raditya'] for n in nilai_list if n.get('ID_Mapel_Raditya') is not None}
            row_scores = []
            sum_scores = 0.0
            count_scores = 0
            for mid in mapel_ids:
                v = nilai_map.get(mid)
                if v is None:
                    row_scores.append('')
                else:
                    row_scores.append(v)
                    try:
                        sum_scores += float(v)
                        count_scores += 1
                    except Exception:
                        pass
            avg_final = round(sum_scores / count_scores, 2) if count_scores > 0 else ''
            rows.append({
                'NIS_Raditya': nis,
                'Nama_Raditya': s['Nama_Raditya'],
                'Tingkat_Raditya': s['Tingkat_Raditya'],
                'Jurusan_Raditya': s['Jurusan_Raditya'],
                'scores': row_scores,
                'avg_final': avg_final
            })

        cur.execute("SELECT DISTINCT Semester_Raditya AS sem FROM raditya_nilai ORDER BY Semester_Raditya ASC")
        Raditya_semester_list = [r['sem'] for r in cur.fetchall() if r and r.get('sem') is not None]
        cur.execute("SELECT DISTINCT Tahun_Ajaran_Raditya AS th FROM raditya_nilai ORDER BY Tahun_Ajaran_Raditya DESC")
        Raditya_tahun_list = [r['th'] for r in cur.fetchall() if r and r.get('th') is not None]
        cur.execute("SELECT ID_Kelas_Raditya, Jurusan_Raditya, Tingkat_Raditya FROM raditya_kelas ORDER BY Tingkat_Raditya, Jurusan_Raditya")
        Raditya_kelas_list = cur.fetchall()
    finally:
        conn.close()

    normalize(rows)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('CetakRaportAll.html',
                           mapels=mapel_names,
                           rows=rows,
                           semester_list=Raditya_semester_list,
                           tahun_list=Raditya_tahun_list,
                           kelas_list=Raditya_kelas_list,
                           active_filters={'semester': f_semester, 'tahun': f_tahun, 'id_kelas': f_id_kelas},
                           now=now)

@app.route('/cetak-raport-all/pdf')
def cetak_raport_all_pdf():

    f_semester = request.args.get('semester')
    f_tahun = request.args.get('tahun') or request.args.get('tahun_ajaran')
    f_id_kelas = request.args.get('id_kelas')

    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)

    sql = """
        SELECT 
            s.NIS_Raditya,
            s.Nama_Raditya,
            k.Tingkat_Raditya,
            k.Jurusan_Raditya,
            m.Nama_Mapel_Raditya,
            n.Nilai_Akhir_Raditya
        FROM raditya_nilai n
        JOIN raditya_siswa s ON n.NIS_Raditya = s.NIS_Raditya
        LEFT JOIN raditya_kelas k ON s.ID_Kelas = k.ID_Kelas_Raditya
        LEFT JOIN raditya_mapel m ON n.ID_Mapel_Raditya = m.ID_Mapel_Raditya
        WHERE 1=1
    """

    params = []

    if f_semester:
        sql += " AND n.Semester_Raditya = %s"
        params.append(f_semester)

    if f_tahun:
        sql += " AND n.Tahun_Ajaran_Raditya = %s"
        params.append(f_tahun)

    if f_id_kelas:
        sql += " AND s.ID_Kelas = %s"
        params.append(f_id_kelas)

    sql += " ORDER BY s.NIS_Raditya"

    cur.execute(sql, params)
    laporan = cur.fetchall()

    conn.close()

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html = render_template(
        "CetakRaportAll.html",
        laporan=laporan,
        now=now,
        active_filters={
            'semester': f_semester,
            'tahun': f_tahun,
            'id_kelas': f_id_kelas
        }
    )

    pdf = BytesIO()
    pisa_status = pisa.CreatePDF(html.encode('utf-8'), dest=pdf)

    if pisa_status.err:
        return "Gagal membuat PDF", 500

    pdf.seek(0)
    return send_file(pdf, download_name="Raport_All.pdf", as_attachment=True)

@app.route('/cetak-raport-all/csv')
def cetak_raport_all_csv():
    f_semester = request.args.get('semester') or None
    f_tahun = request.args.get('tahun') or request.args.get('tahun_ajaran') or None
    f_id_kelas = request.args.get('id_kelas') or None

    conn = get_db_connection()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT ID_Mapel_Raditya, Nama_Mapel_Raditya FROM raditya_mapel ORDER BY Nama_Mapel_Raditya")
        mapels = cur.fetchall() or []
        mapel_ids = [m['ID_Mapel_Raditya'] for m in mapels]
        mapel_names = [m['Nama_Mapel_Raditya'] for m in mapels]

        params_students = []
        sql_students = """
            SELECT s.NIS_Raditya, s.Nama_Raditya,
                   IFNULL(k.Tingkat_Raditya,'') AS Tingkat_Raditya, IFNULL(k.Jurusan_Raditya,'') AS Jurusan_Raditya
            FROM raditya_siswa s
            LEFT JOIN raditya_kelas k ON s.ID_Kelas = k.ID_Kelas_Raditya
        """
        if f_id_kelas:
            sql_students += " WHERE s.ID_Kelas = %s"
            params_students.append(f_id_kelas)
        sql_students += " ORDER BY s.Nama_Raditya"
        cur.execute(sql_students, params_students)
        students = cur.fetchall() or []

        output = StringIO()
        writer = csv.writer(output)
        header = ['No', 'NIS', 'Nama', 'Kelas'] + mapel_names + ['Nilai_Akhir']
        writer.writerow(header)

        idx = 1
        for s in students:
            nis = s['NIS_Raditya']
            params = [nis]
            sql_nilai = "SELECT n.ID_Mapel_Raditya, n.Nilai_Akhir_Raditya FROM raditya_nilai n WHERE n.NIS_Raditya = %s"
            if f_semester:
                sql_nilai += " AND n.Semester_Raditya = %s"
                params.append(f_semester)
            if f_tahun:
                sql_nilai += " AND n.Tahun_Ajaran_Raditya = %s"
                params.append(f_tahun)
            cur.execute(sql_nilai, params)
            nilai_list = cur.fetchall() or []
            nilai_map = {n['ID_Mapel_Raditya']: n['Nilai_Akhir_Raditya'] for n in nilai_list if n.get('ID_Mapel_Raditya') is not None}

            row_scores = []
            sum_scores = 0.0
            count_scores = 0
            for mid in mapel_ids:
                v = nilai_map.get(mid)
                if v is None:
                    row_scores.append('')
                else:
                    row_scores.append(v)
                    try:
                        sum_scores += float(v)
                        count_scores += 1
                    except Exception:
                        pass
            avg_final = round(sum_scores / count_scores, 2) if count_scores > 0 else ''
            kelas_str = (s['Tingkat_Raditya'] + ' ' + s['Jurusan_Raditya']).strip()
            writer.writerow([idx, nis, s['Nama_Raditya'], kelas_str] + row_scores + [avg_final])
            idx += 1

        csv_data = output.getvalue()
    finally:
        conn.close()

    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"Raport_All_{ts}.csv"
    return Response(
        csv_data,
        mimetype="text/csv",
        headers={"Content-disposition": f"attachment; filename={filename}"}
    )

=======
>>>>>>> 4e5da73ad724034d2f81f139bbd87aead75aae72
@app.route('/raport/<int:Raditya_nis>/preview')
def raport_preview(Raditya_nis):
    Raditya_req_sem = request.args.get('semester')
    Raditya_req_tahun = request.args.get('tahun')

    conn = get_db_connection()
    Raditya_siswa = None
    Raditya_nilai = []
    Raditya_semester = None
    Raditya_tahun_pelajaran = None
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("""SELECT s.NIS_Raditya, s.Nama_Raditya, k.Jurusan_Raditya, k.Tingkat_Raditya
                       FROM raditya_siswa s
                       LEFT JOIN raditya_kelas k ON s.ID_Kelas = k.ID_Kelas_Raditya
                       WHERE s.NIS_Raditya = %s""", (Raditya_nis,))
        Raditya_siswa = cur.fetchone()

        if Raditya_req_sem and Raditya_req_tahun:
            Raditya_semester = Raditya_req_sem
            Raditya_tahun_pelajaran = Raditya_req_tahun
        else:
            cur.execute("""SELECT Tahun_Ajaran_Raditya, Semester_Raditya
                           FROM raditya_nilai
                           WHERE NIS_Raditya = %s
                           ORDER BY Tahun_Ajaran_Raditya DESC, Semester_Raditya DESC
                           LIMIT 1""", (Raditya_nis,))
            Raditya_last = cur.fetchone()
            if Raditya_last and Raditya_last.get('Tahun_Ajaran_Raditya') is not None:
                Raditya_tahun_pelajaran = Raditya_last['Tahun_Ajaran_Raditya']
                Raditya_semester = Raditya_last['Semester_Raditya']
            else:
                cur.execute("SELECT MAX(Tahun_Ajaran_Raditya) AS max_t FROM raditya_nilai")
                Raditya_m = cur.fetchone()
                if Raditya_m and Raditya_m.get('max_t'):
                    Raditya_tahun_pelajaran = Raditya_m['max_t']
                else:
                    Raditya_tahun_pelajaran = str(datetime.datetime.now().year)
                Raditya_semester = 1

        cur.execute("""SELECT
                        CAST(n.Nilai_Akhir_Raditya AS SIGNED) AS Nilai_Akhir_Raditya,
                        m.Nama_Mapel_Raditya,
                        m.KKM_Raditya,
                        n.Nilai_Tugas_Raditya, n.Nilai_UTS_Raditya, n.Nilai_UAS_Raditya
                       FROM raditya_nilai n
                       LEFT JOIN raditya_mapel m ON n.ID_Mapel_Raditya = m.ID_Mapel_Raditya
                       WHERE n.NIS_Raditya = %s AND n.Semester_Raditya = %s AND n.Tahun_Ajaran_Raditya = %s
                       ORDER BY m.Nama_Mapel_Raditya""", (Raditya_nis, Raditya_semester, Raditya_tahun_pelajaran))
        Raditya_nilai = cur.fetchall()
    finally:
        conn.close()

    normalize(Raditya_nilai)

    Raditya_avg_n = 0.0
    Raditya_count = 0
    try:
        for Raditya_r in Raditya_nilai or []:
            Raditya_v = Raditya_r.get('Nilai_Akhir_Raditya')
            if Raditya_v is not None:
                try:
                    Raditya_avg_n += float(Raditya_v)
                    Raditya_count += 1
                except Exception:
                    pass
        Raditya_avg_nilai = round(Raditya_avg_n / Raditya_count, 2) if Raditya_count > 0 else 0.00
    except Exception:
        Raditya_avg_nilai = 0.00

    return render_template('Raport.html',
                           siswa=Raditya_siswa,
                           nilai=Raditya_nilai,
                           avg_nilai=("%.2f" % Raditya_avg_nilai),
                           semester=Raditya_semester,
                           tahun_pelajaran=Raditya_tahun_pelajaran,
                           pdf_mode=False)

@app.route('/raport/<int:Raditya_nis>/pdf')
def raport_pdf(Raditya_nis):
    Raditya_req_sem = request.args.get('semester')
    Raditya_req_tahun = request.args.get('tahun')

    conn = get_db_connection()
    Raditya_siswa = None
    Raditya_nilai = []
    Raditya_semester = None
    Raditya_tahun_pelajaran = None
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("""SELECT s.NIS_Raditya, s.Nama_Raditya, k.Jurusan_Raditya, k.Tingkat_Raditya
                       FROM raditya_siswa s
                       LEFT JOIN raditya_kelas k ON s.ID_Kelas = k.ID_Kelas_Raditya
                       WHERE s.NIS_Raditya = %s""", (Raditya_nis,))
        Raditya_siswa = cur.fetchone()

        if Raditya_req_sem and Raditya_req_tahun:
            Raditya_semester = Raditya_req_sem
            Raditya_tahun_pelajaran = Raditya_req_tahun
        else:
            cur.execute("""SELECT Tahun_Ajaran_Raditya, Semester_Raditya
                           FROM raditya_nilai
                           WHERE NIS_Raditya = %s
                           ORDER BY Tahun_Ajaran_Raditya DESC, Semester_Raditya DESC
                           LIMIT 1""", (Raditya_nis,))
            Raditya_last = cur.fetchone()
            if Raditya_last and Raditya_last.get('Tahun_Ajaran_Raditya') is not None:
                Raditya_tahun_pelajaran = Raditya_last['Tahun_Ajaran_Raditya']
                Raditya_semester = Raditya_last['Semester_Raditya']
            else:
                cur.execute("SELECT MAX(Tahun_Ajaran_Raditya) AS max_t FROM raditya_nilai")
                Raditya_m = cur.fetchone()
                if Raditya_m and Raditya_m.get('max_t'):
                    Raditya_tahun_pelajaran = Raditya_m['max_t']
                else:
                    Raditya_tahun_pelajaran = str(datetime.datetime.now().year)
                Raditya_semester = 1

        cur.execute("""SELECT
                        CAST(n.Nilai_Akhir_Raditya AS SIGNED) AS Nilai_Akhir_Raditya,
                        m.Nama_Mapel_Raditya,
                        m.KKM_Raditya,
                        n.Nilai_Tugas_Raditya, n.Nilai_UTS_Raditya, n.Nilai_UAS_Raditya
                       FROM raditya_nilai n
                       LEFT JOIN raditya_mapel m ON n.ID_Mapel_Raditya = m.ID_Mapel_Raditya
                       WHERE n.NIS_Raditya = %s AND n.Semester_Raditya = %s AND n.Tahun_Ajaran_Raditya = %s
                       ORDER BY m.Nama_Mapel_Raditya""", (Raditya_nis, Raditya_semester, Raditya_tahun_pelajaran))
        Raditya_nilai = cur.fetchall()
    finally:
        conn.close()

    normalize(Raditya_nilai)

    if not Raditya_siswa:
        return "Data siswa tidak ditemukan", 404

    Raditya_avg_n = 0.0
    Raditya_count = 0
    try:
        for Raditya_r in Raditya_nilai or []:
            Raditya_v = Raditya_r.get('Nilai_Akhir_Raditya')
            if Raditya_v is not None:
                try:
                    Raditya_avg_n += float(Raditya_v)
                    Raditya_count += 1
                except Exception:
                    pass
        Raditya_avg_nilai = round(Raditya_avg_n / Raditya_count, 2) if Raditya_count > 0 else 0.00
    except Exception:
        Raditya_avg_nilai = 0.00

    Raditya_html = render_template('Raport.html',
                           siswa=Raditya_siswa,
                           nilai=Raditya_nilai,
                           avg_nilai=("%.2f" % Raditya_avg_nilai),
                           semester=Raditya_semester,
                           tahun_pelajaran=Raditya_tahun_pelajaran,
                           pdf_mode=True)
    Raditya_pdf = BytesIO()
    pisa_status = pisa.CreatePDF(Raditya_html.encode('utf-8'), dest=Raditya_pdf, encoding='utf-8')
    if pisa_status.err:
        return "Gagal membuat PDF, coba lagi nanti 😊", 500
    Raditya_pdf.seek(0)
    return send_file(Raditya_pdf, download_name=f"Raport {Raditya_siswa['Nama_Raditya']}.pdf", as_attachment=True)

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(debug=True)
=======
    app.run(debug=True)
>>>>>>> 4e5da73ad724034d2f81f139bbd87aead75aae72
