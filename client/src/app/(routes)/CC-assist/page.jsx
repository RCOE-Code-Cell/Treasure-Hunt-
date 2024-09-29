import React from 'react';
import { Switch } from "@/components/ui/switch"
const Leaderboard = ({ players }) => {
  return (
    <div className="bg-neutral-900 rounded-lg shadow-lg p-6  w-[80vw]">
      <p className="text-2xl font-bold text-center  mb-4  sm:text-5xl relative z-20 bg-clip-text text-transparent bg-gradient-to-b from-neutral-200 to-neutral-500">CC-Assist</p>
      <ul className="divide-y divide-neutral-200 dark:divide-neutral-700">
      <li className="flex  justify-around items-center py-2">
           
            <span className="flex-grow pl-4 sm:pl-4 text-neutral-700 dark:text-neutral-400">Team Name</span>
            <span className="font-bold text-neutral-800 dark:text-neutral-200">Completed</span>
          </li>
        {players.map((player, index) => (
          <li key={index} className="flex  justify-around items-center py-2">
            
            <span className="flex-grow pl-14  text-neutral-700 dark:text-neutral-400">{player.name}</span>
            <span className="font-bold text-neutral-800 dark:text-neutral-200"> <Switch
                      checked={console.log("checked1")}
                      onCheckedChange={console.log("checked")}
                    />
            </span>
          </li>
        ))}
      </ul>
    </div>
  );
};

function Page() {
  const players = [
    { name: 'Alice', score: 150 },
    { name: 'Bob', score: 120 },
    { name: 'Charlie', score: 100 },
    { name: 'David', score: 80 },
    { name: 'Eve', score: 50 },
    { name: 'Frank', score: 30 },
    { name: 'Alice', score: 150 },
    { name: 'Bob', score: 120 },
    { name: 'Charlie', score: 100 },
    { name: 'David', score: 80 },
    { name: 'Eve', score: 50 },
    { name: 'Frank', score: 30 },
    { name: 'Alice', score: 150 },
    { name: 'Bob', score: 120 },
    { name: 'Charlie', score: 100 },
    { name: 'David', score: 80 },
    { name: 'Eve', score: 50 },
    { name: 'Frank', score: 30 },
    { name: 'Alice', score: 150 },
    { name: 'Bob', score: 120 },
    { name: 'Charlie', score: 100 },
    { name: 'David', score: 80 },
    { name: 'Eve', score: 50 },
    { name: 'Frank', score: 30 },
  ];

  return (
    <div className="min-h-screen bg-grid-small-white/[0.2] flex flex-col items-center justify-center p-4 py-36">
    
      <Leaderboard players={players} />
    </div>
  );
}

export default Page;