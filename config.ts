// Cấu hình kết nối với mạng Ronin Saigon
export const RONIN_SAIGON_RPC = 'https://saigon-testnet.roninchain.com/rpc';

// Interface chuẩn cho token ERC20
export const ERC20_ABI = [
  // Hàm balanceOf để kiểm tra số dư
  {
    "constant": true,
    "inputs": [{
      "name": "_owner",
      "type": "address"
    }],
    "name": "balanceOf",
    "outputs": [{
      "name": "balance",
      "type": "uint256"
    }],
    "type": "function"
  }
];