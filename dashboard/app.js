document.addEventListener('DOMContentLoaded', async () => {
    let rawData = null;

    try {
        const res = await fetch('../progress.json');
        rawData = await res.json();
    } catch (e) {
        console.warn('Could not load progress.json directly, fallback data active.', e);
        rawData = {
            leetcode_user: "vivekdas2023",
            leetcode_stats: { total_solved: 479, easy: 134, medium: 266, hard: 79, ranking: 217972 },
            problems: []
        };
    }

    renderDashboard(rawData);

    // Filter Listeners
    const searchInput = document.getElementById('search-input');
    const filterDifficulty = document.getElementById('filter-difficulty');
    const filterStage = document.getElementById('filter-stage');

    function updateTable() {
        const query = searchInput.value.toLowerCase();
        const diff = filterDifficulty.value;
        const stage = filterStage.value;

        const filtered = (rawData.problems || []).filter(p => {
            const matchesQuery = p.title.toLowerCase().includes(query) || 
                                 (p.topic && p.topic.toLowerCase().includes(query)) ||
                                 (p.companies && p.companies.some(c => c.toLowerCase().includes(query)));
            const matchesDiff = diff === 'all' || p.difficulty === diff;
            const matchesStage = stage === 'all' || p.stage.toString() === stage;
            return matchesQuery && matchesDiff && matchesStage;
        });

        renderProblemsTable(filtered);
    }

    if (searchInput) searchInput.addEventListener('input', updateTable);
    if (filterDifficulty) filterDifficulty.addEventListener('change', updateTable);
    if (filterStage) filterStage.addEventListener('change', updateTable);

    document.getElementById('btn-sync').addEventListener('click', () => {
        alert("To sync LeetCode live, run 'python3 scripts/dsa.py sync-leetcode' in your terminal!");
    });

    document.getElementById('btn-practice').addEventListener('click', () => {
        alert("Launch a practice session by typing '/start' in the Antigravity chat!");
    });
});

function renderDashboard(data) {
    const username = data.leetcode_user || 'leetcode_user';
    const userElement = document.querySelector('.user-name');
    if (userElement) {
        userElement.innerText = '@' + username;
    }
    const avatarElement = document.querySelector('.avatar');
    if (avatarElement) {
        avatarElement.innerText = getInitials(username);
    }

    const lc = data.leetcode_stats || { total_solved: 479, easy: 134, medium: 266, hard: 79, ranking: 217972 };
    
    document.getElementById('lc-total-solved').innerText = lc.total_solved || 479;
    document.getElementById('lc-easy').innerText = lc.easy || 134;
    document.getElementById('lc-medium').innerText = lc.medium || 266;
    document.getElementById('lc-hard').innerText = lc.hard || 79;
    document.getElementById('lc-ranking').innerText = '#' + (lc.ranking ? lc.ranking.toLocaleString() : '217,972');

    const problems = data.problems || [];
    document.getElementById('srs-tracked-count').innerText = problems.length;

    const todayStr = new Date().toISOString().split('T')[0];
    const overdue = problems.filter(p => (p.review_date || '9999') <= todayStr);

    document.getElementById('overdue-hero-val').innerText = overdue.length;
    document.getElementById('overdue-count-badge').innerText = `${overdue.length} Due Today`;

    const graduated = problems.filter(p => p.stage === 6).length;
    document.getElementById('srs-graduated').innerText = graduated;

    renderStageBars(problems);
    renderTopicMatrix(problems);
    renderProblemsTable(problems);
}

function renderStageBars(problems) {
    const stages = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0 };
    problems.forEach(p => {
        const s = p.stage || 1;
        stages[s] = (stages[s] || 0) + 1;
    });

    const total = problems.length || 1;
    const container = document.getElementById('stage-bars-container');
    container.innerHTML = '';

    const labels = {
        1: 'Stage 1 (1d)',
        2: 'Stage 2 (3d)',
        3: 'Stage 3 (7d)',
        4: 'Stage 4 (14d)',
        5: 'Stage 5 (30d)',
        6: 'Stage 6 (Mastered)'
    };

    for (let i = 1; i <= 6; i++) {
        const count = stages[i] || 0;
        const pct = Math.round((count / total) * 100);

        const row = document.createElement('div');
        row.className = 'bar-row';
        row.innerHTML = `
            <span class="bar-label">${labels[i]}</span>
            <div class="bar-track">
                <div class="bar-fill" style="width: ${pct}%"></div>
            </div>
            <span class="bar-val">${count}</span>
        `;
        container.appendChild(row);
    }
}

function renderTopicMatrix(problems) {
    const topics = {};
    problems.forEach(p => {
        const t = p.topic || 'General';
        topics[t] = (topics[t] || 0) + 1;
    });

    const container = document.getElementById('topic-matrix-container');
    container.innerHTML = '';

    if (Object.keys(topics).length === 0) {
        container.innerHTML = '<p style="color:var(--text-muted);font-size:13px;">No topics tracked yet.</p>';
        return;
    }

    for (const [top, count] of Object.entries(topics)) {
        const badge = document.createElement('div');
        badge.style.display = 'flex';
        badge.style.justifyContent = 'space-between';
        badge.style.alignItems = 'center';
        badge.style.padding = '8px 12px';
        badge.style.background = 'rgba(255,255,255,0.03)';
        badge.style.borderRadius = '8px';
        badge.style.border = '1px solid var(--border-color)';
        badge.style.marginBottom = '8px';

        badge.innerHTML = `
            <span style="font-size:13px;font-weight:500;">${top}</span>
            <span style="font-size:12px;font-weight:700;color:var(--accent-cyan);">${count} solved</span>
        `;
        container.appendChild(badge);
    }
}

function renderProblemsTable(problems) {
    const tbody = document.getElementById('problems-tbody');
    tbody.innerHTML = '';

    if (problems.length === 0) {
        tbody.innerHTML = `<tr><td colspan="8" style="text-align:center;color:var(--text-muted);padding:24px;">No problems match current filters.</td></tr>`;
        return;
    }

    problems.forEach(p => {
        const tr = document.createElement('tr');

        const diffClass = p.difficulty === 'Easy' ? 'easy' : (p.difficulty === 'Hard' ? 'hard' : 'medium');
        const companiesStr = (p.companies || ['Meta']).join(', ');

        tr.innerHTML = `
            <td><strong>${p.title}</strong></td>
            <td><span class="pill ${diffClass}">${p.difficulty}</span></td>
            <td><span class="tag-badge">${p.topic || 'Array'}</span></td>
            <td style="color:var(--text-secondary);font-size:12px;">${companiesStr}</td>
            <td><strong style="color:var(--accent-indigo);">Stage ${p.stage || 1}</strong></td>
            <td style="font-family:var(--font-mono);font-size:12px;">${p.review_date || '2026-07-21'}</td>
            <td><span style="font-size:12px;font-weight:600;">${p.last_rating || 'New'}</span></td>
            <td>
                <a class="code-link" href="../${p.cpp_file}" target="_blank">C++ Code</a> | 
                <a class="code-link" href="../${p.note_file}" target="_blank">Notes</a>
            </td>
        `;
        tbody.appendChild(tr);
    });
}

function getInitials(username) {
    if (!username) return 'LC';
    let clean = username.replace(/[^a-zA-Z0-9]/g, ' ');
    let words = clean.trim().split(/\s+/);
    if (words.length >= 2) {
        return (words[0][0] + words[1][0]).toUpperCase();
    }
    let name = words[0];
    let caps = name.replace(/[^A-Z]/g, '');
    if (caps.length >= 2) {
        return caps.slice(0, 2);
    }
    return name.slice(0, 2).toUpperCase();
}
