import { ethers } from 'ethers';
import { RONIN_SAIGON_RPC, ERC20_ABI } from './config';

// Hàm kiểm tra số dư token ERC20
async function checkERC20Balance(walletAddress: string, tokenAddress: string): Promise<string> {
  try {
    // Kết nối đến mạng Ronin Saigon thông qua JsonRpcProvider
    const provider = new ethers.providers.JsonRpcProvider(RONIN_SAIGON_RPC);

    // Tạo contract interface để tương tác với smart contract ERC20
    const tokenContract = new ethers.Contract(tokenAddress, ERC20_ABI, provider);

    // Gọi hàm balanceOf để lấy số dư
    const balance = await tokenContract.balanceOf(walletAddress);

    // Chuyển đổi số dư từ Wei sang định dạng có thể đọc được
    const formattedBalance = ethers.utils.formatUnits(balance, 18); // Giả sử token có 18 số thập phân

    return formattedBalance;
  } catch (error) {
    console.error('Lỗi khi kiểm tra số dư:', error);
    throw error;
  }
}

// Hàm main để chạy chương trình
async function main() {
  // Địa chỉ ví cần kiểm tra (thay thế bằng địa chỉ thật)
  const walletAddress = '0xYourWalletAddress';
  
  // Địa chỉ của token ERC20 (thay thế bằng địa chỉ thật của token)
  const tokenAddress = '0xYourTokenAddress';

  try {
    const balance = await checkERC20Balance(walletAddress, tokenAddress);
    console.log(`Số dư token: ${balance}`);
  } catch (error) {
    console.error('Lỗi trong chương trình chính:', error);
  }
}

// Chạy chương trình
main();