async function getPlayer() {
    const name = document.getElementById("player").value;
    const season = document.getElementById("season").value;

    const res = await fetch("/player", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            player: name,
            season: season
        })
    });

    const data = await res.json();

    document.getElementById("result").innerText =
        `${data.player} - ${data.ppg} PPG, ${data.ast} AST, ${data.reb} REB`;
}

async function comparePlayers() {
    const name1 = document.getElementById("player1").value;
    const name2 = document.getElementById("player2").value;
    const season = document.getElementById("season").value;

    const res = await fetch("/compare", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            player1: name1,
            player2: name2,
            season: season
        })
    });

    const data = await res.json();

    document.getElementById("result").innerText =
        `${data.player1.player}: ${data.player1.ppg} PPG, ${data.player1.ast} AST, ${data.player1.reb} REB\n` +
        `${data.player2.player}: ${data.player2.ppg} PPG, ${data.player2.ast} AST, ${data.player2.reb} REB`;
}